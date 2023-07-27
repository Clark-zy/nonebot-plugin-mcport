from asyncio import open_connection, StreamReader, StreamWriter
from typing import Optional
from .rcon import Rcon
from .excepts import ClientError, InvalidPassword


class MinecraftClient:
    host: Optional[str]
    port: Optional[int]
    pasw: Optional[str]

    _reader: Optional[StreamReader]
    _writer: Optional[StreamWriter]

    auth_state: bool = False
    """是否登陆"""
    init_state: bool = False
    """是否初始化"""
    cone_state: bool = False
    """是否链接"""

    def __init__(self, host: str, port: int, pasw: str):
        self.host = host
        self.port = port
        self.pasw = pasw

        self._reader: StreamReader = None
        self._writer: StreamWriter = None

        self.init_state = True

    async def _read_data(self, leng):
        """读取数据"""

        data = b''
        while len(data) < leng:
            data += await self._reader.read(leng - len(data))

        return data

    async def _read(self):
        """读取并解析数据"""
        packet = await Rcon.async_read_packet(self._read_data)

        if packet.packet_end != Rcon.END:
            raise ClientError('链接异常！')

        if packet.packet_id == -1:
            raise InvalidPassword('密码无效！')

        return packet.data

    async def _send(self, packet):
        """发送数据包, 并返回结果"""

        if not self._writer:
            raise ClientError('尚未创建链接, 请使用connect方法创建链接！')

        # 发送数据
        self._writer.write(packet)
        return await self._read()

    async def _connect(self):
        """创建链接"""

        if not self.init_state:
            raise ClientError('尚未初始化, 请使用connect方法创建链接！')

        if self.auth_state:
            raise ClientError('已登陆, 请直接使用send方法发送数据！')

        try:
            self._reader, self._writer = await open_connection(self.host, self.port)
        except OSError as e:
            raise ClientError('无法创建链接: {}'.format(e))
        self.cone_state = True

    async def __aenter__(self):
        await self._connect()
        await self.auth()

        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    @classmethod
    async def connect(cls, *, host, port, pasw):
        """初始化链接并登陆, 返回链接对象"""
        self = cls(host, port, pasw)

        # 创建链接
        await self._connect()
        # 登陆
        await self.auth()

        return self

    async def close(self):
        """关闭链接"""
        if self._writer:
            self._writer.close()
            self._writer = None
            self._auth = False

    async def auth(self, pasw: str = None):
        """
        登陆 未创建链接直接登录会自动创建链接
        """
        pasw = pasw or self.pasw
        
        if not self.cone_state:
            await self._connect()

        """登陆"""
        if not self.auth_state:
            packet = Rcon.auth(pasw)
            await self._send(packet)
            self.auth_state = True

    async def command(self, command):
        """发送命令"""
        packet = Rcon.command(command)
        return await self._send(packet)

    async def say(self, message):
        """发送聊天"""
        await self.command(f"say {message}")
