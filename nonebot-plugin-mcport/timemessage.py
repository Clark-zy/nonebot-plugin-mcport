import nonebot
from nonebot import require
from nonebot import get_driver, logger
#获取群号配置
config = get_driver().config.dict()
timemessage = config.get('timemessage')
#定时发送消息，群号配置在.env自行配置
# 设置一个定时器
timing = require("nonebot_plugin_apscheduler").scheduler
@timing.scheduled_job("cron", hour='06', minute = '00' , second = '00' ,id="dingshi")
async def _():
    #这里是获取bot对象
    (bot,) = nonebot.get_bots().values()
    await bot.send_msg(
        message_type="group",
        group_id=timemessage,
        message="起床了！！！"
    )
