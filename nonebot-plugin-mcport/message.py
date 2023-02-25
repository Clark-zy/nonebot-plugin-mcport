from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event,MessageSegment

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
    
cz=on_keyword({"充值"},block=True,priority=5)

@cz.handle()
async def _():
    await cz.finish(Message("充值请前往爱发电主页\nhttps://afdian.net/a/jskjfwq/plan\n购买对应点券后查看爱发电私信即可\n游戏内购买完商品后，请查看商店左下角邮箱领取"))
