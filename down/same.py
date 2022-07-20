from yt_dlp import YoutubeDL


def Down_video(path, detail):
    # down
    URLS = detail["url"]

    ydl_opts = {
        'noplaylist': True,
        'format': 'bestaudio',
        "outtmpl": path + '%(title)s.%(ext)s'
    }
    if detail["type"] == "mp4":
        ydl_opts["format"] = None
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)
    else:
        ydl_opts["outtmpl"] = path + '%(title)s.mp3'
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)