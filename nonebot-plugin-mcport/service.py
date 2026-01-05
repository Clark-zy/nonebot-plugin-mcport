from typing import Optional
from nonebot import get_driver
from nonebot.log import logger
from .config import RCONConfig
from .rcon_client import AutoReconnectRCON

class RCONService:
    """RCON服务"""
    
    def __init__(self):
        # 获取全局配置
        driver = get_driver()
        self.config = RCONConfig(
            rcon_host=getattr(driver.config, "rcon_host", "localhost"),
            rcon_port=getattr(driver.config, "rcon_port", 25575),
            rcon_password=getattr(driver.config, "rcon_password", ""),
            rcon_timeout=getattr(driver.config, "rcon_timeout", 5),
            rcon_max_retries=getattr(driver.config, "rcon_max_retries", 3),
            rcon_retry_delay=getattr(driver.config, "rcon_retry_delay", 3)
        )
        self._client: Optional[AutoReconnectRCON] = None
        
    async def init_client(self) -> bool:
        """初始化RCON客户端"""
        self._client = AutoReconnectRCON(
            host=self.config.rcon_host,
            port=self.config.rcon_port,
            password=self.config.rcon_password,
            timeout=self.config.rcon_timeout,
            max_retries=self.config.rcon_max_retries,
            retry_delay=self.config.rcon_retry_delay
        )
        
        return await self._client.connect()
    
    async def send_command(self, command: str) -> Optional[str]:
        """发送命令（主接口）"""
        if not self._client:
            if not await self.init_client():
                return None
        return await self._client.send_command(command)
    
    async def get_client(self) -> Optional[AutoReconnectRCON]:
        """获取RCON客户端实例"""
        return self._client
    
    async def health_check(self) -> bool:
        """健康检查"""
        if not self._client:
            return await self.init_client()
        return await self._client.test_connection()

rcon_service = RCONService()