from down.win import Down as win_down1
from down.linux import biliili_down as linux_down
import os

"""
开始文件
"""
if __name__ == '__main__':
    # url:B站视频
    while True:
        Type = "mp4"
        type_dict = {"1": "mp4", "2": "mp3"}
        print(type_dict)
        word = input("请输入获取类型,默认为MP4,不修改请直接回车")
        if word == "":
            pass
        else:
            Type = type_dict[word]

        URL = []
        print("请输入视频网址(可多个)\n", end="")
        while True:
            Url = input()
            if Url == "":
                break
            else:
                URL.append(Url)

        detail_inputs = {
            "url": URL,
            "type": Type
        }

        if os.name == 'nt':
            win_down1(detail_inputs)
        elif os.name == 'posix':
            linux_down(detail_inputs)
