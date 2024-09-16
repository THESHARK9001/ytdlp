import yt_dlp
import os
from os import path
import shutil
def youtube_downloader():
    fullpath = os.path.join
    python_directory = "./videos"
    start_directory = "./"
    URLS = input("Link: ")
    ydl_opts = {
        'format': 'ba+bv',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)
    if not path.exists("./videos"):
        os.mkdir("./videos")
    def main():
        for dirname, dirnames, filenames in os.walk(start_directory):
            for filename in filenames:
                source = fullpath(dirname, filename)
                if filename.endswith("mp4"):
                    shutil.move(source, fullpath(python_directory, filename))
    main()
youtube_downloader()
