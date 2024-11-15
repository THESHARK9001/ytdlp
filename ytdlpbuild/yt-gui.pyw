import yt_dlp
from tkinter import *
from tkinter import ttk
def youtube():
    root.title("Shark's YTDLP script (Downloading...)")
    URLS = video_link.get()
    ydl_opts = {
        'format': 'bv+ba',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)
    root.title("Shark's YTDLP script (Ready)")
root = Tk()
root.title("Shark's YTDLP script (Ready)")
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
