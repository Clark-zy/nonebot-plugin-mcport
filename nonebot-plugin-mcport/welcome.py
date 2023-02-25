from nonebot import get_driver
from nonebot import on_request
from nonebot.typing import T_State
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import ActionFailed
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent
from nonebot_plugin_txt2img import Txt2Img
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent, MessageSegment, GroupDecreaseNoticeEvent
import json
#####自定义发图配置
config = get_driver().config.dict()
tit = config.get("tit")
font_size = 32
txt2img = Txt2Img()
txt2img.set_font_size(font_size)
title = tit
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
tit = config.get("tit")

welcom = on_notice()
# 群友入群
@welcom.handle()  # 监听 welcom
async def h_r(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):  # event: GroupIncreaseNoticeEvent  群成员增加事件
    user = event.get_user_id()  # 获取新成员的id
    at_ = "[CQ:at,qq={}]".format(user)
    text = '欢迎新成员 加入我们的大家族!\n首次进入需要申请白名单:\n申请白名单 id\n游戏教程以及异常处理请前往网站查看\njiushu.info'
    pic = txt2img.draw(title, text)
    msg_1 = MessageSegment.image(pic)
    msg=at_ + text
    if event.group_id in groupset:
        try:
            await welcom.finish(message=Message(f'{msg}'))  # 发送消息
        except ActionFailed:
            await welcom.finish(message=Message(f'{msg_1}'))

# 群友退群
@welcom.handle()
async def h_r(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):  # event: GroupDecreaseNoticeEvent  群成员减少事件
    user = event.get_user_id()  # 获取新成员的id
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '这位玩家离开了本群，大家快出来送别它吧！'
    msg = Message(msg)
    if event.group_id in groupset:
        await welcom.finish(message=Message(f'{msg}'))  # 发送消息
