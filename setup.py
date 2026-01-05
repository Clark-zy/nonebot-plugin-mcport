from setuptools import find_packages, setup
import os
path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(path, "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()
    setup(name='nonebot-plugin-mcport',
          version='0.1.1',
          description='通过RCON向我的世界JAVA服务器发送命令.',
          long_description=long_description,
          long_description_content_type="text/markdown",
          author='Provias',
          author_email='1686886163@qq.com',
          url='http://wwww.clarkhub.cn',
          include_package_data=True,
          install_requires=[
              "loguru",
              "pydantic_settings",
              "numpy",
              "nonebot2>=2.0.0a16",
              "nonebot-adapter-onebot>=2.0.0b1",
              "nonebot-plugin-apscheduler>=0.2.0"
          ],
          license='MIT License',
          packages=find_packages(),
          platforms=["all"],
          classifiers=['Intended Audience :: Developers',
                       'Operating System :: OS Independent',
                       'Natural Language :: Chinese (Simplified)',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3.8',
                       'Programming Language :: Python :: 3.9',
                       'Topic :: Software Development :: Libraries'
                       ],
          )

