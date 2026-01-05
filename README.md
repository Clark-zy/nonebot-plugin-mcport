# 请保护好自己的rcon配置项，任何问题与本插件无关
* 一个可以远程操控我的世界java服务器的bot
* 关于如何使用
# 前提(必要)
1. 在服务端根目录server.properties内添加三个配置项
2. rcon.port=
3. rcon.password=
4. enable-rcon=true
# 我的世界功能部分
1.   请务必保护好自己的rcon信息，此信息为你的敏感信息
2.   在.env中配置服务器的rcon项

# 功能介绍
1. 向我的世界java服务器发送可自定义的命令并返回信息

# env配置项
| config | example | usage | 
| -------- | -------- | -------- | 
| RCON_HOST| RCON_HOST = "127.0.0.1"| 服务器ip|
| RCON_PORT| RCON_PORT = | 服务器rcon端口 | 
| RCON_PASSWORD| RCON_PASSWORD = ""| 服务器rcon密码| 
|RCON_MAX_RETRIES| RCON_MAX_RETRIES=5| rcon连接失败后最大重连次数| 
| RCON_RETRY_DELAY|RCON_RETRY_DELAY=5 | 每次重连向后推迟5秒| 



