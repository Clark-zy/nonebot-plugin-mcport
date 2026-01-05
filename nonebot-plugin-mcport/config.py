from pydantic_settings import BaseSettings
from typing import Optional

class RCONConfig(BaseSettings):
    """RCON配置"""
    rcon_host: str = "localhost"  # RCON服务器地址
    rcon_port: int = 25575        # RCON端口
    rcon_password: str = ""       # RCON密码
    rcon_timeout: int = 5         # 超时时间（秒）
    rcon_max_retries: int = 3     # 最大重试次数
    rcon_retry_delay: int = 3     # 重试延迟（秒）
    
    class Config:
        env_prefix = ""  # 环境变量前缀
        case_sensitive = False