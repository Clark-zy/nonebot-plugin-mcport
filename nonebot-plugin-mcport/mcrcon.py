from nonebot import get_driver
from nonebot.log import logger
from nonebot import on_command, on_regex
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
from nonebot.params import RegexGroup
import re
from . import service as mc_rcon
config = get_driver().config.dict()
serverowner = config.get("serverowner")#获取服务器管理员QQ

# 默认全员可用指令list
list = on_command("list")
@list.handle()
async def main():
    list_output = await mc_rcon.send_command("list")
    if list_output is None:
        await list.finish(message=Message(f'连接服务器失败\n,请稍等'))
    text = re.sub(r"§\w", "", list_output)#去除颜色代码
    await list.send(message=Message(f'{text}'))
 
    
# 向服务端发送指令(只能由serverowner进行)
zxml = on_regex(r"^执行命令\s*(.+)?")
@zxml.handle()
async def mingling(event: GroupMessageEvent, w=RegexGroup()):
    event1 = w[0] #获取指令
    if event.user_id not in serverowner:
        await zxml.finish("权限等级不足")     
    output = await mc_rcon.send_command(f"{event1}")
    if output:
        text = re.sub(r"§\w", "", output)
        await zxml.finish(message=Message(f'{text}'))
    else:
        await zxml.finish("命令已发送，无回执")

