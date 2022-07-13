from down.win import down as win_down1
from down.linux import biliili_down as linux_down
import os

"""
开始文件
"""
if __name__ == '__main__':
    # url:B站视频
    URL=[]
    print("请输入视频网址\n")
    while True:
        Url = input()
        if Url is "":
            break
        else:
            URL.append(Url)

    # Path:存储目录，最好是空的
    Path = ""
    ffmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
    Type = "mp4"
    detail_inputs = {
        "url": URL,
        "path": Path,
        "ffmpeg": ffmpeg,
        "type": Type
    }

    if os.name is 'nt':
        win_down1(detail_inputs)
    elif os.name is 'posix':
        linux_down(detail_inputs)