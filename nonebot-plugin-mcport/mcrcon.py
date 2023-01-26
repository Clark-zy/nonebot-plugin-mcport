from async_mcrcon import MinecraftClient
from nonebot import on_keyword
from nonebot import get_driver
from nonebot import on_request
from nonebot.typing import T_State
from nonebot import on_notice
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent
from nonebot.permission import SUPERUSER, Permission
from nonebot import on_command, on_regex
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event, GroupIncreaseNoticeEvent, MessageSegment, GroupDecreaseNoticeEvent
from nonebot.params import CommandArg, RegexGroup
import asyncio
import re
import json



############画图部分
############画图部分
############画图部分
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from pathlib import Path
from nonebot.adapters.onebot.v11 import MessageSegment as MS


def text_to_img(
    text: str, font_path: str = f"{Path(__file__).parent}/font/HYWenHei-85W.ttf"
) -> BytesIO:
    """
    字转图片
    """
    lines = text.splitlines()
    line_count = len(lines)
    # 读取字体
    font = ImageFont.truetype(font_path, 18)
    # 获取字体的行高
    left, top, width, line_height = font.getbbox("a")
    # 增加行距
    line_height += 3
    # 获取画布需要的高度
    height = line_height * line_count + 20
    # 获取画布需要的宽度
    width = int(max([font.getlength(line) for line in lines])) + 25
    # 字体颜色
    black_color = (0, 0, 0)
    # 生成画布
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    # 按行开画，c是计算写到第几行
    c = 0
    for line in lines:
        draw.text((10, 6 + line_height * c), line, font=font, fill=black_color)
        c += 1
    img_bytes = BytesIO()
    image.save(img_bytes, format="jpeg")
    return img_bytes
############画图结束

#画图测试
test = on_regex(r"^test$")
@test.handle()
async def handle_test(event: GroupMessageEvent, mp=RegexGroup()):
    text = """画图测试"""
    await test.finish(MS.image(text_to_img(text)))
#画图测试

############插件正文
############插件正文
############插件正文


# 获取服务器rcon配置
config = get_driver().config.dict()
rconhost = config.get("rconhost")
rconport = config.get("rconport")
rconpassword = config.get("rconpassword")
zr = config.get("zr")
# 命令部分
# list
list = on_command("list")
@list.handle()
async def main():
    async with MinecraftClient(rconhost, rconport, rconpassword) as mc:
        output = await mc.send("list")
        await list.finish(MS.image(text_to_img((re.sub(r"§\w", "", output)))))


# 向服务端发送指令(只能由zr进行)
zxml = on_regex(r"^执行命令\s*(.+)?")
@zxml.handle()
async def mingling(event: GroupMessageEvent, w=RegexGroup()):
    event1 = w[0]
    print(w)
    if event1 and event.user_id==zr:       
        user_id = event.user_id
        async with MinecraftClient(rconhost, rconport, rconpassword) as mc:
            output = await mc.send(f"{event1}")
            if output:
                len(output) > 0
                await zxml.finish(MS.image(text_to_img((re.sub(r"§\w", "", output)))))
            else:
                await zxml.finish("命令已发送，无回执")
    else:
        await zxml.finish("癞蛤蟆想吃天鹅肉，你小子在想什么？")

# 申请白名单(白名单添加)
whitelist_apply = on_regex(r"^申请白名单\s*(\S+)?")
@whitelist_apply.handle()
async def mcink(event: GroupMessageEvent, mp=RegexGroup()):
    player_id = mp[0]
    if player_id:
        user_id = event.user_id
        async with MinecraftClient(rconhost, rconport, rconpassword) as mc:
            output = await mc.send(f"mcink add {user_id} {player_id}")
            await whitelist_apply.finish(MS.image(text_to_img((re.sub(r"§\w", "", output)))))
    else:
        await whitelist_apply.finish("申请白名单 你的id")


#这里是无脑自动同意进群
#这里是无脑自动同意进群
#这里是无脑自动同意进群
#这里是无脑自动同意进群
#这里是无脑自动同意进群
notice=on_request(priority=1)
group_to_use=[""] #填开启自动审批的群
@notice.handle()
async def _(bot: Bot,event: GroupRequestEvent):
    raw = json.loads(event.json())
    gid = str(event.group_id)
    flag = raw['flag']
    sub_type = raw['sub_type']
    if sub_type == 'add':
            comment = raw['comment']
            word = re.findall(re.compile('答案：(.*)'), comment)[0]
            uid = event.user_id
            await bot.set_group_add_request(         
                    flag=flag,
                    sub_type=sub_type,
                    approve=True,
                    reason=" ",
                )
    else:
        await notice.finish("鸡掰，无脑通过怎么会出现else情况呢？")
        
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
    at_ = "欢迎新成员[CQ:at,qq={}]".format(user)
    msg = '欢迎新成员 加入我们的大家族!\n首次进入需要申请白名单:\n申请白名单 id\n游戏教程以及异常处理请前往网站查看\njiushu.info'
    msg = Message(msg)
    print(at_)
    if event.group_id == groupset:
        await welcom.finish(MS.image(text_to_img(f'{msg}')))  # 发送消息

# 群友退群
@welcom.handle()
async def h_r(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):  # event: GroupDecreaseNoticeEvent  群成员减少事件
    user = event.get_user_id()  # 获取新成员的id
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '这位玩家离开了本群，大家快出来送别它吧！'
    msg = Message(msg)
    print(at_)

    if event.group_id == groupset:
        await welcom.finish(message=Message(f'{msg}'))  # 发送消息


#随意名字=on_notice(rule=_rule)
#同上随意名字.handle()
#async def group_increase_handle(event: GroupIncreaseNoticeEvent):
    #user = event.get_user_id()
    #at_ = "欢迎新成员[CQ:at,qq={}]".format(user)
    #msg = at_ + '欢迎新成员 加入我们的大家族!\n首次进入需要申请白名单:\n申请白名单 id\n游戏教程以及异常处理请前往网站查看\njiushu.info'
    #msg = Message(msg)
    #print(at_)
    #if event.group_id == groupset2:
        #await 同上随意名字.finish(message=Message(f'{msg}')) 

##自动回复部分
toushi=on_keyword({"透视"})

@toushi.handle()
async def _():
    await toushi.finish(Message("手机端透视:在设置-视频设置-性能-快速渲染关掉即可\n电脑端透视:砸了换手机"))

huaping=on_keyword({"花屏"})

@huaping.handle()
async def _():
    await huaping.finish(Message("请前往https://jiushu.info/help/\n查看具体教程"))


