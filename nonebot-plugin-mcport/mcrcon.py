from async_mcrcon import MinecraftClient
from nonebot import on_keyword
from nonebot import get_driver
from nonebot import on_request
from nonebot.typing import T_State
from nonebot import on_notice
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent
from nonebot.permission import SUPERUSER, Permission
from nonebot_plugin_txt2img import Txt2Img
from nonebot import on_command, on_regex
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event, GroupIncreaseNoticeEvent, MessageSegment, GroupDecreaseNoticeEvent
from nonebot.params import CommandArg, RegexGroup
import asyncio
import re
import json

# 获取服务器rcon配置
config = get_driver().config.dict()
rconhost = config.get("rconhost")
rconport = config.get("rconport")
rconpassword = config.get("rconpassword")
zr = config.get("zr")
tit = config.get("tit")
# list
list = on_command("list")
@list.handle()
async def main():
    async with MinecraftClient(rconhost, rconport, rconpassword) as mc:
        output = await mc.send("list")
        title = tit
        text = re.sub(r"§\w", "", output)
        font_size = 32
        txt2img = Txt2Img()
        txt2img.set_font_size(font_size)
        pic = txt2img.draw(title, text)
        msg = MessageSegment.image(pic)
        await list.finish(message=Message(f'{msg}'))


# 向服务端发送指令(只能由SUPERUSER进行)
zxml = on_regex(r"^执行命令\s*(.+)?")
@zxml.handle()
async def mingling(event: GroupMessageEvent, w=RegexGroup()):
    event1 = w[0]
    print(w)
    print(zr)
    if event1 and event.user_id in zr:       
        user_id = event.user_id
        async with MinecraftClient(rconhost, rconport, rconpassword) as mc:
            output = await mc.send(f"{event1}")
            if output:
                len(output) > 0
                title = tit
                text = re.sub(r"§\w", "", output)
                font_size = 32
                txt2img = Txt2Img()
                txt2img.set_font_size(font_size)
                pic = txt2img.draw(title, text)
                msg = MessageSegment.image(pic)
                await zxml.finish(message=Message(f'{msg}'))
            else:
                await zxml.finish("命令已发送，无回执")
    else:
        await zxml.finish("癞蛤蟆想吃天鹅肉，你小子在想什么？")

# 申请白名单(白名单添加)
whitelist_apply = on_regex(r"^申请白名单\s*(\S+)?")
@whitelist_apply.handle()
async def mcink(event: GroupMessageEvent,mp=RegexGroup()):
    player_id = mp[0]
    if player_id:
        user_id = event.user_id
        async with MinecraftClient(rconhost, rconport, rconpassword) as mc:
            output = await mc.send(f"mcink add {user_id} {player_id}")
            title = tit
            text = re.sub(r"§\w", "", output)
            font_size = 32
            txt2img = Txt2Img()
            txt2img.set_font_size(font_size)
            pic = txt2img.draw(title, text)
            msg = MessageSegment.image(pic)
            await whitelist_apply.finish(message=Message(f'{msg}'))
    else:
        await whitelist_apply.finish("申请白名单 你的id")


#这里是无脑自动同意进群
#这里是无脑自动同意进群
#这里是无脑自动同意进群
#这里是无脑自动同意进群
#这里是无脑自动同意进群
notice=on_request(priority=1)
@notice.handle()
async def _(bot: Bot,event: GroupRequestEvent):
    raw = json.loads(event.json())
    user_info = await bot.get_stranger_info(user_id=event.user_id)
    logger.info(user_info)
    flag = raw['flag']
    sub_type = raw['sub_type']
    if sub_type == 'add':
            level = user_info["level"]
            int(level)
            if level >= 10:
                await bot.set_group_add_request(flag=flag,sub_type=sub_type,approve=True)
            else:
                await bot.set_group_add_request(flag=flag,sub_type=sub_type,approve=False,reason='QQ等级小于10级，如误判，请联系管理员')               
    else:
        await notice.finish()
    await notice.finish()


#这里是入群欢迎捏
#获取群号配置
#开启多群模式在.env配置groupset2=群号,并在此插件下方做相应配置
config = get_driver().config.dict()
groupset = config.get('groupset')

welcom = on_notice()
# 群友入群
@welcom.handle()  # 监听 welcom
async def h_r(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):  # event: GroupIncreaseNoticeEvent  群成员增加事件
    user = event.get_user_id()  # 获取新成员的id
    title = tit
    text = '欢迎新成员 加入我们的大家族!\n首次进入需要申请白名单:\n申请白名单 id\n游戏教程以及异常处理请前往网站查看\njiushu.info'
    font_size = 32
    txt2img = Txt2Img()
    txt2img.set_font_size(font_size)
    pic = txt2img.draw(title, text)
    msg = MessageSegment.image(pic)
    if event.group_id in groupset:
        await welcom.finish(message=Message(f'{msg}'))  # 发送消息

# 群友退群
@welcom.handle()
async def h_r(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):  # event: GroupDecreaseNoticeEvent  群成员减少事件
    user = event.get_user_id()  # 获取新成员的id
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '这位玩家离开了本群，大家快出来送别它吧！'
    msg = Message(msg)
    if event.group_id in groupset:
        await welcom.finish(message=Message(f'{msg}'))  # 发送消息
##自动回复部分
toushi=on_keyword({"透视"},block=True,priority=1)

@toushi.handle()
async def _():
    await toushi.finish(Message("手机端透视:在设置-视频设置-性能-快速渲染关掉即可\n电脑端透视:砸了换手机"))

huaping=on_keyword({"花屏"},block=True,priority=2)

@huaping.handle()
async def _():
    await huaping.finish(Message("请前往https://jiushu.info/help/\n查看具体教程"))
    
daoyubaohu=on_keyword({"岛屿保护"},block=True,priority=3)

@daoyubaohu.handle()
async def _():
    await daoyubaohu.finish(Message("有岛屿保护情况的\n输入is reset和is confirm后即可\n还不行的，多输入几次就可以"))
    

ban=on_keyword({"ban表"},block=True,priority=4)

@ban.handle()
async def _():
    await ban.finish(Message("游戏内输入warp show即可查看ban表"))    



