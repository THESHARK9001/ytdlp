# Imports
import yt_dlp, os, shutil
from os import path
from tkinter import *
from tkinter import ttk

# Functions
def youtube():
    fullpath = os.path.join
    python_directory = "./videos"
    start_directory = "./"

    URLS = video_link.get()

    ydl_opts = {
        'format': 'bv+ba',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)

    if not path.exists("./videos"):
        os.mkdir("./videos")

    def main():
        for dirname, dirnames, filenames in os.walk(start_directory):
            for filename in filenames:
                source = fullpath(dirname, filename)
                if filename.endswith(".webm"):
                    shutil.move(source, fullpath(python_directory, filename))
    main()

root = Tk()
root.title("Shark's YTDLP script")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

link = StringVar()

video_link = ttk.Entry(mainframe, width=50, textvariable=link)
ttk.Button(mainframe, text="Download", command=youtube).grid(column = 2, row = 2, sticky=W)
ttk.Label(mainframe, text="Link:").grid(column = 1, row = 1, sticky=W)
video_link.grid(column = 2, row = 1, sticky = W)

root.mainloop()
