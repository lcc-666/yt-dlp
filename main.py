from down.win import down

"""
开始文件
"""
if __name__ == '__main__':
    # url:B站视频
    Url = "https://www.bilibili.com/video/BV1U3411k7VV?p=4&vd_source=161d770991feb7a2b647ccb79f47e675"
    # Path:存储目录，最好是空的
    Path = ""
    ffmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
    Type="mp3"
    detail_inputs = {
        "url": Url,
        "path": Path,
        "ffmpeg": ffmpeg,
        "type": Type
    }
    down(detail_inputs)
