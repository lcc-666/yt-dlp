from down.win import down

"""
开始文件
"""
if __name__ == '__main__':
    # url:B站视频
    Url = "https://www.bilibili.com/video/BV1aY4y1B74o?spm_id_from=333.851.b_7265636f6d6d656e64.1"
    # Path:存储目录，最好是空的
    Path = ""
    ffmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
    detail_inputs = {
        "url": Url,
        "path": Path,
        "ffmpeg": ffmpeg
    }
    down(detail_inputs)
