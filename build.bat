@echo Please make sure you have python installed before continuing
@pause
@echo Please make sure you do not have a VPN while using yt.py 
@pause
@set /p "build=1 (CLI) or 2 (GUI) > "
@if %build%==1 (	
	@python.exe -m pip install --upgrade pip
	@pip install yt-dlp pyinstaller
	@pyinstaller --clean --onefile --icon=.\ytdlpbuild\Icon.ico .\ytdlpbuild\yt.py
	@del yt.spec
	@echo y|rmdir /s build
	@copy .\dist\yt.exe .\yt.exe
	@echo y|rmdir /s dist
	@pause
)
@if %build%==2 (	
	@python.exe -m pip install --upgrade pip
	@pip install yt-dlp pyinstaller
	@pyinstaller --clean --onefile --icon=.\ytdlpbuild\Icon.ico .\ytdlpbuild\yt-gui.py
	@del yt-gui.spec
	@y|rmdir /s build
	@copy .\dist\yt-gui.exe .\yt-gui.exe
	@y|rmdir /s dist
	@pause
)