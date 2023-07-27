from .mcrcon import MinecraftClient as MinecraftClient
from .excepts import ClientError, InvalidPassword


# 上下文用法
# async with MinecraftClient(host='localhost', port=25575, pasw='AABBCC') as client:

#     result = await client.say('weather rain')
#     print(result)

#     result = await client.command('help')
#     print(result)


# 简单用法
# client = await MinecraftClient.connect(host='localhost', port=25575, pasw='AABBCC')

# result = await client.say('weather rain')
# print(result)

# result = await client.command('help')
# print(result)

# await client.close()
