from nonebot import get_driver
from nonebot import logger
from rcon import MinecraftClient, ClientError, InvalidPassword

driver = get_driver()

config = get_driver().config.dict()
rconhost = config.get("rconhost")
rconport = config.get("rconport")
rconpassword = config.get("rconpassword")

MCClient = MinecraftClient(host=rconhost, port=rconport, pasw=rconpassword)

@driver.on_startup()
async def rcon_connect():
    try:
        await MCClient.auth()
    except ClientError as e:
        logger.warning(f'Rcon 服务连接失败！{e.msg}')
    else:
        logger.info('Rcon 服务已连接')

@driver.on_shutdown()
async def rcon_close():
    await MCClient.close()
    logger.info('Rcon 服务已关闭')