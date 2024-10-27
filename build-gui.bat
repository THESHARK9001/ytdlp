@echo Please make sure you have python installed before continuing
@pause
@echo Please make sure you do not have a VPN while using yt-gui.py 
@pause
@python.exe -m pip install --upgrade pip
@pip install yt-dlp pyinstaller
@pyinstaller --clean --onefile --noconsole .\ytdlpbuild\yt-gui.pyw
@del yt-gui.spec
@echo y|rmdir /s build
@copy .\dist\yt-gui.exe .\yt-gui.exe
@echo y|rmdir /s dist
@pause
