from distutils.core import setup
from setuptools import find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='nonebot-plugin-mcport',  
      version='1.0.0',  
      description='通过RCON向我的世界JAVA服务器发送命令',
      author='Provias',
      author_email='1686886163@qq.com',
      url='https://github.com/Proviasw/nonebot-plugin-mcport',
      license='MIT License',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',        
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries'
      ],
      python_requires='>=3.8',
      install_requires=[
        "nonebot2>=2.0.0rc1,<3.0.0",
        "nonebot-adapter-onebot>=2.1.5"
    ]
)