class RconBaseError(Exception):
    """Rcon错误"""
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

class ClientError(RconBaseError):
    """链接错误"""
    pass

class InvalidPassword(RconBaseError):
    """登陆错误"""
    pass
