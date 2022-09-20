# DeezerMusicDownload
The aim of this project is to provide fast music download without my management.
Downloading albums or specific songs from Deezer is possible on Telegram using the Deezer Music Bot chat.
However, it is not possible to download a playlist. Since I have playlists with a lot of songs (almost a thousand), 
manually downloading them would take a lot of time and energy.
That's why I wrote the code that does all that for me.
## How To Run Scripts
I used a Python programming language and a Selenium library.
The code consists of two scripts and one .txt file.
The process starts by running the <b>deezer_main.py</b> script, where a user in the console enters the link of the playlist.
A web page of the playlist opens up in a Chrome browser window and share links of all songs from the Deezer playlist are being collected and stored in the <b>links_file.txt</b> file.

- <b>IMPORTANT</b>
  
  The <b>playlist</b> that the user wants to download must be <b>public</b>. Also, the user should <b>expand the browser window</b> so there wouldn't be any errors. 

After the deezer_main.py script is finished, the user runs <b>telegram_main.py</b> script, which opens a Chrome browser window with the displayed QR code
through which the user logs in to Telegram. 

- <b>IMPORTANT</b>
  
  The first thing the user needs to do after logging in to Telegram
is to open the <b>already started</b> Deezer Music Bot chat.
  It means that user has already clicked the <b>start</b> option once in the <b>Deezer Music Bot</b> chat before running the script.
Also, in the meantime, it is necessary to <b>enable multiple downloading</b> on the browser.

The script sends all share links from links_file.txt to the Deezer Music Bot and downloads songs that Deezer Music Bot sends back to the user.
When the program is finished, log out from Telegram and find the downloaded music on your computer.