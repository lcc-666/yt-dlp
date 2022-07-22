# yt-dlp
一个基于yt-dlp的python程序，在yt-dlp上进行了简单的封装，将不常用的功能封装，只留下一些常用的功能。
(已经添加多url抓取)

### 环境准备
建议使用[python官网](https://www.python.org/)3.7/8版本
(已去除ffmpeg,使用yt-dlp自带的合并,但是需要提前配置)

win

![image](https://user-images.githubusercontent.com/81516638/179966612-db56e129-a4b4-4bac-8b84-cd7f00c6e848.png)

配置到ffmpeg的bin目录

Ubuntu

我是用Ubuntu20.04做测试(apt下载ffmpeg)

sudo apt install ffmpeg

![image](https://user-images.githubusercontent.com/81516638/179967059-34aebc9c-f835-4928-8463-dbec23b31597.png)


### 客户端环境
博主再win和Linux上进行了基本测试mac未经过测试。

###  文件安装
本程序基于yt-dlp

pip install yt-dlp

git clone https://github.com/lcc-666/yt-dlp.git




### IDE
本人使用[pycharm](https://www.jetbrains.com/pycharm/)进行编辑

在main.py中进行基本的配置,由于网络问题,主要用BiliBili做抓取测试。

```python
from down.win import down as win_down1
from down.linux import biliili_down as linux_down
import os

"""
开始文件
"""
if __name__ == '__main__':
    # url:B站视频
    URL = []
    print("请输入视频网址(可多个)\n", end="")
    while True:
        Url = input()
        if Url is "":
            break
        else:
            URL.append(Url)

    Type = "mp3"
    detail_inputs = {
        "url": URL,
        "type": Type
    }

    if os.name is 'nt':
        win_down1(detail_inputs)
    elif os.name is 'posix':
        linux_down(detail_inputs)
```

![image](https://user-images.githubusercontent.com/81516638/179391874-af3910cf-44dc-4f42-8584-b8769b2fcec2.png)
![image](https://user-images.githubusercontent.com/81516638/179391902-d7b57b9e-ccb6-4272-b2a0-8fe028c2b437.png)


### 本地快速打包
```
pip install pyinstaller
```
先确保代码可以正常运行

![image](https://user-images.githubusercontent.com/81516638/179967781-b80ef5ab-2614-4da0-83bb-cfc5d7fb3b70.png)

直接运行即可。

![image](https://user-images.githubusercontent.com/81516638/179967873-65774ea3-74ad-48e9-beef-dbd801585a87.png)


![image](https://user-images.githubusercontent.com/81516638/180415800-c64a3d68-7a23-4b17-9ad4-bdd96d9902be.png)





