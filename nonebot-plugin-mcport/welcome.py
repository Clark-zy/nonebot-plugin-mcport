from nonebot import get_driver
from nonebot import on_request
from nonebot.typing import T_State
from nonebot import on_notice
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent
import json
#####自定义发图配置
config = get_driver().config.dict()

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
                await bot.set_group_add_request(flag=flag,sub_type=sub_type,approve=False,reason='QQ等级小于10级,如误判,请联系管理员')               
    else:
        await notice.finish()
    await notice.finish()


#这里是入群欢迎
#获取群号配置
#开启多群模式在.env配置groupset2=群号,并在此插件下方做相应配置
config = get_driver().config.dict()
groupset = config.get('groupset')

welcom = on_notice()
# 群友入群
@welcom.handle()  # 监听 welcom
async def h_r(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):  # event: GroupIncreaseNoticeEvent  群成员增加事件
    user = event.get_user_id()  # 获取新成员的id
    at_ = "[CQ:at,qq={}]".format(user)
    text = '欢迎新成员 加入我们的大家族!\n首次进入需要申请白名单:\n申请白名单 id\n进入游戏需配置三方登录,请前往clarkhub.cn查看\n'
    msg=at_ + text
    await welcom.finish(message=Message(f'{msg}'))  # 发送消息


# 群友退群
@welcom.handle()
async def h_r(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):  # event: GroupDecreaseNoticeEvent  群成员减少事件
    user = event.get_user_id()  # 获取新成员的id
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '这位玩家离开了本群，大家快出来送别它吧！'
    msg = Message(msg)
    await welcom.finish(message=Message(f'{msg}'))  # 发送消息
