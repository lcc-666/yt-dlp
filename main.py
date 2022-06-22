from down.win import down

"""
开始文件
"""
if __name__ == '__main__':
    # url:B站视频
    Url = input("请输入视频网址\n")
    # Path:存储目录，最好是空的
    Path = ""
    ffmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
    Type = "mp3"
    detail_inputs = {
        "url": Url,
        "path": Path,
        "ffmpeg": ffmpeg,
        "type": Type
    }
    down(detail_inputs)
