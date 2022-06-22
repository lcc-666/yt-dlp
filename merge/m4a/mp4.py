from ffmpy3 import FFmpeg


# 合并视频和音频
def merge(inputs, save_path, title, ffmpeg_path):
    ff = FFmpeg(
        executable=ffmpeg_path,
        inputs=inputs,
        outputs={save_path + title + ".mp4": None}
    )
    ff.run()


# MP4转换MP3
def tomp3(inputs, save_path, title, ffmpeg_path):
    ff = FFmpeg(
        executable=ffmpeg_path,
        inputs=inputs,
        outputs={save_path + title + ".mp3": None}
    )
    ff.run()


if __name__ == '__main__':
    path = r"D:\learn\pythonproject\biliili\down\\"
    video = "腾讯发布会1500_页的PPT，到底高级在哪儿？【旁门左道】.mp4"
    audio = "腾讯发布会1500_页的PPT，到底高级在哪儿？【旁门左道】.m4a"
    ffmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
