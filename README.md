# 请保护好自己的rcon配置项，任何问题与本插件无关
* 一个可以远程操控我的世界java服务器的bot
* 此插件配置视频教程：[点我查看视频教程](https://www.bilibili.com/video/BV1LY411S7kD/?share_source=copy_web&vd_source=e0ca427d4461aaedc892cf4bc908d052)
* 关于如何使用
# 前提(必要)
* 克隆整个仓库,将本目录下的async_mcrcon.py放入site-packages目录下
* 虚拟环境同理，放入python包路径即可
* pip install pillow
* pip install async-mcrcon
* nb plugin install nonebot-plugin-txt2img
# 我的世界功能部分
1.   请务必保护好自己的rcon信息，此信息为你的敏感信息
2.   在.env中配置服务器的rcon项
# bot配置
* 配置一个go-cq端作为无头QQ端
# 主体部分
* 自行配置nonebot2客户端，具体教程参考b站小狐狸[点此跳转nb2配置教程](https://www.bilibili.com/read/cv21231223?spm_id_from=333.999.0.0)
# 功能介绍
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
# env配置项
| config | example | usage | 
| -------- | -------- | -------- | 
| rconhost| rconhost = "127.0.0.1"| 服务器ip|
| rconpassword| rconpassword = "114514"| 服务器rcon密码 | 
| rconpor| rconport = 114514| 服务器rcon端口| 
|groupset| groupset=[114514]| 开启入群欢迎的群号| 
| zr|zr=[1919810] | 响应执行命令的主人QQ号| 
|tit|tit=仙贝|图片的title| 



