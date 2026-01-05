import asyncio
import socket
from typing import Optional, Tuple
from loguru import logger
from mcrcon import MCRcon

class AutoReconnectRCON:
    
    def __init__(
        self,
        host: str,
        port: int,
        password: str,
        timeout: int = 5,
        max_retries: int = 3,
        retry_delay: int = 3
    ):
        self.host = host
        self.port = port
        self.password = password
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self._client: Optional[MCRcon] = None
        self._connected = False
        
    async def connect(self) -> bool:
        """连接RCON服务器"""
        for attempt in range(1, self.max_retries + 1):
            try:
                logger.info(f"尝试连接RCON服务器 {self.host}:{self.port} (第{attempt}次)")
                
                self._client = MCRcon(self.host, self.password, port=self.port)
                
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, self._client.connect)
                
                self._connected = True
                logger.success(f"成功连接到RCON服务器 {self.host}:{self.port}")
                return True
                
            except (socket.timeout, ConnectionRefusedError, ConnectionResetError) as e:
                logger.warning(f"连接失败: {e}")
                
                if attempt < self.max_retries:
                    logger.info(f"{self.retry_delay}秒后重试...")
                    await asyncio.sleep(self.retry_delay)
                else:
                    logger.error(f"达到最大重试次数({self.max_retries})，连接失败")
                    
            except Exception as e:
                logger.error(f"连接RCON时发生错误: {e}")
                break
                
        self._connected = False
        return False
    
    async def send_command(self, command: str) -> Optional[str]:
        if not self._connected or not self._client:
            logger.warning("RCON未连接，尝试重新连接...")
            if not await self.connect():
                return None
        
        try:
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                self._client.command, 
                command
            )
            return response
            
        except (socket.timeout, ConnectionResetError, BrokenPipeError) as e:
            logger.warning(f"连接中断: {e}，尝试重连...")
            self._connected = False
            
            if await self.connect():
                return await self.send_command(command)
            else:
                return None
                
        except Exception as e:
            logger.error(f"发送命令时发生错误: {e}")
            return None
    
    async def test_connection(self) -> bool:
        try:
            response = await self.send_command("list")
            return response is not None
        except:
            return False
    
    def is_connected(self) -> bool:
        return self._connected
    
    async def disconnect(self):
        if self._client:
            try:
                self._client.disconnect()
            except:
                pass
            finally:
                self._client = None
                self._connected = False
        logger.info("RCON连接已断开")