from async_mcrcon import MinecraftClient
from nonebot import get_driver
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import ActionFailed
from nonebot_plugin_txt2img import Txt2Img
from nonebot import on_command, on_regex
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.params import RegexGroup
import re

# 获取服务器rcon配置
config = get_driver().config.dict()
rconhost = config.get("rconhost")
rconport = config.get("rconport")
rconpassword = config.get("rconpassword")
zr = config.get("zr")
tit = config.get("tit")
#####发图配置
title=tit
font_size = 32
txt2img = Txt2Img()
txt2img.set_font_size(font_size)
# list
list = on_command("list")
@list.handle()
async def main():
    try:
        async with MinecraftClient(rconhost, rconport, rconpassword) as mc:
            output = await mc.send("list")
            text = re.sub(r"§\w", "", output)
            pic = txt2img.draw(title, text)
            msg = MessageSegment.image(pic)
            await list.send(message=Message(f'{text}'))
    except ConnectionRefusedError:
        await list.send(message=Message(f'连接服务器失败\n可能是服务器在重启，请稍后再试'))
    except ActionFailed:
        logger.info(f'消息风控，所以我切换了发图捏')
        await list.send(message=Message(f'{msg}'))
 
            


    

# 向服务端发送指令(只能由SUPERUSER进行)
zxml = on_regex(r"^执行命令\s*(.+)?")
@zxml.handle()
async def mingling(event: GroupMessageEvent, w=RegexGroup()):
    event1 = w[0]
    logger.info(f'有人触发"执行命令"指令了哦~')
    if event.user_id in zr:       
        user_id = event.user_id
        try:
            async with MinecraftClient(rconhost, rconport, rconpassword) as mc:
                output = await mc.send(f"{event1}")
                if output:
                    len(output) > 0
                    text = re.sub(r"§\w", "", output)
                    pic = txt2img.draw(title, text)
                    msg = MessageSegment.image(pic)
                    await zxml.finish(message=Message(f'{text}'))
                else:
                    await zxml.finish("命令已发送，无回执")
        except ConnectionRefusedError:
            await zxml.send(message=Message(f'连接服务器失败\n可能是服务器在重启，请稍后再试'))  
        except ActionFailed:
            logger.info(f'消息风控，所以我切换了发图捏')
            await zxml.send(message=Message(f'{msg}'))       
    else:
        await zxml.finish("癞蛤蟆想吃天鹅肉，你小子在想什么？")

# 申请白名单(白名单添加)
whitelist_apply = on_regex(r"^申请白名单\s*(\S+)?")
@whitelist_apply.handle()
async def mcink(event: GroupMessageEvent,mp=RegexGroup()):
    player_id = mp[0]
    if player_id:
        user_id = event.user_id
        try:
            async with MinecraftClient(rconhost, rconport, rconpassword) as mc:
                output = await mc.send(f"mcink add {user_id} {player_id}")
                text = re.sub(r"§\w", "", output)
                pic = txt2img.draw(title, text)
                msg = MessageSegment.image(pic)
                await whitelist_apply.finish(message=Message(f'{text}'))
        except ConnectionRefusedError:   
            await whitelist_apply.send(message=Message(f'连接服务器失败\n可能是服务器在重启，请稍后再试')) 
        except ActionFailed:
            logger.info(f'消息风控，所以我切换了发图捏')
            await whitelist_apply.send(message=Message(f'{msg}'))     
    else:
        await whitelist_apply.finish("申请白名单 你的id")




