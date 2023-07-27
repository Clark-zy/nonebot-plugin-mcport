import struct
from dataclasses import dataclass


class Rcon:
    END = b'\x00\x00'
    """结束符"""

    class PacketType:
        """发送类型"""

        AUTH = 3
        """登陆"""
        COMMAND = 2
        """命令"""
        CHAT = 1
        """聊天"""
        SEND = 0
        """发包"""
        
    @dataclass
    class ReadPacket:
        packet_id: int
        packet_end: bytes
        packet_type: bytes
        data: str

    @staticmethod
    def build_packet(packet_type: 'Rcon.PacketType', data: str):
        """构建数据包"""
        out = struct.pack('<li', 0, packet_type) + \
            data.encode('utf8') + Rcon.END

        out_len = struct.pack('<i', len(out))
        return out_len + out

    @staticmethod
    async def async_read_packet(read_func):
        """
        异步读取数据包

        :param read_func: 读取函数
        :return: (packet_id, packet_end, packet_type, data)
        """
        result = await read_func(4)
        result_len, *_ = struct.unpack('<i', result)
        packet_bytes = await read_func(result_len)

        return Rcon.read_packet(packet_bytes)

    @staticmethod
    def sync_read_packet(read_func):
        """
        同步读取数据包
        :param read_func: 读取函数
        :return: (packet_id, packet_end, packet_type, data)
        """
        result = read_func(4)
        result_len, *_ = struct.unpack('<i', result)
        packet_bytes = read_func(result_len)

        return Rcon.read_packet(packet_bytes)

    @staticmethod
    def read_packet(packet_bytes: bytes):
        """
        解析数据包

        :param packet_bytes: 数据包
        :return: (packet_id, packet_end, packet_type, data)
        """
        packet_id, packet_type = struct.unpack('<ii', packet_bytes[:8])
        packet_data, packet_end = packet_bytes[8:-2], packet_bytes[-2:]

        data = packet_data.decode('utf8')
        return Rcon.ReadPacket(packet_id, packet_end, packet_type, data)

    @staticmethod
    def command(cmd: str):
        """构建命令数据"""
        return Rcon.build_packet(Rcon.PacketType.COMMAND, cmd)

    @staticmethod
    def auth(pasw: str):
        """构建登陆数据"""
        return Rcon.build_packet(Rcon.PacketType.AUTH, pasw)
