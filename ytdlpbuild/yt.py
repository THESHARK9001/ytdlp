import yt_dlp
def youtube_downloader():
    URLS = input("Link: ")
    ydl_opts = {
        'format': 'bv+ba',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)
youtube_downloader()
