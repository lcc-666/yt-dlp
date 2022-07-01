from down.win import down as win_down1
from down.linux import biliili_down as linux_down

"""
开始文件
"""
if __name__ == '__main__':
    # url:B站视频
    Url = input("请输入视频网址\n")
    # Path:存储目录，最好是空的
    Path = ""
    ffmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
    Type = "mp4"
    detail_inputs = {
        "url": Url,
        "path": Path,
        "ffmpeg": ffmpeg,
        "type": Type
    }
    #win_down1(detail_inputs)
    linux_down(detail_inputs)