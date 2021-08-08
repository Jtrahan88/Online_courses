"""
Webbrower module
The runs this code using a batch file. The book shows us how to go into our enviromental setting to
set up the path but it must be out dated. Due to that does not work, and there are about 5-7 different ways
I have seen it done on youtube.

I can make the batch file and click it manually only.



"""

import sys, pyperclip, webbrowser

sys.argv
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
# where the url must go
# https://www.google.com/maps/place/ <address>
webbrowser.open('https://www.google.com/maps/place/' + address)



# 150 Airpark Blvd, Chico, CA 95973