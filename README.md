* 一个可以远程操控我的世界java服务器的bot
* 关于如何使用
# 前提(必要)
* 克隆整个仓库,将本目录下的async_mcrcon.py放入site-packages目录下
* 虚拟环境同理，放入python包路径即可
* pip install pillow
* pip install async-mcrcon(如果不存在，请换pip官方源)
# 我的世界功能部分
1.   请务必保护好自己的rcon信息，此信息为你的敏感信息
2.   在.env中配置服务器的rcon项
# bot配置
* 配置一个go-cq端作为无头QQ端
# 主体部分
1. 自行配置nonebot2客户端，具体教程参考b站小狐狸[点此跳转nb2配置教程](https://www.bilibili.com/read/cv21231223?spm_id_from=333.999.0.0)
2. 配置完成后在.env添加如下配置项
3. rconhost = "此处填写你的ip"
4. rconpassword = "此处填写你的password"
5. rconport = 此处填写你的端口
6. groupset = 将本消息替换为需要开启入群欢迎的群号
7. timemessage = 需要开启定时消息的群号
8. zr=填写主人QQ号(不要乱填，会向服务端发送指令)
9. 在此目录下运行nb run即可
# 功能介绍(1-4配置详情mcrcon.py 5配置详情timemessage.py)
1. 向我的世界JAVA版服务端发送指令并返回图片回执
2. 无脑同意进群(需要在mcrcon.py中124行处配置群号)
3. 响应关键词回复
4. 入群欢迎
5. 定时消息
# 如何开启rcon配置
1. 在服务端根目录server.properties内添加三个配置项
2. rcon.port=
3. rcon.password=
4. enable-rcon=true


