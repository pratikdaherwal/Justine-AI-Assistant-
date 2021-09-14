# Add Spotify in query to play songs (online).

import webbrowser
from sys import platform
if platform == "linux" or platform == "linux2":
    chrome_path = '/usr/bin/google-chrome'
elif platform == "darwin":
    chrome_path = 'open -a /Applications/Google\ Chrome.app'
elif platform == "win32":
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
else:
    print('Unsupported OS')
    exit(1)
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab('https://open.spotify.com')
