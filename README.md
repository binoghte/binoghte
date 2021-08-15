- 👋 Hi, I’m @binoghte
- 👀 I’m interested in hacking and programming
- 📫 How to reach me mamad0761@gmail.com


This is my first project on github
Its a whatsapp qrljacker.
It works with firefox and chrome.

in firefox, session will not be saved .I'm looking for a good way to save it in next updates.
in chrome you can set user-data-dir so the session remain if you close chrome. but for taking screen shot chrome will focus repeatly and it's annoying.

how to it works:
It runs a browser under selenium firefox/chrome(you need chrome driver compatible with your chrome version) and extract qrl code of web.whatsapp.com 
then runs an http server on port 80.just send your ip as a link to victim.
index.html page in htdocs folder is a clone of web.whatsapp.com and repeadly reload qrl code that extracted and saved as htdocs/screenshot.png by run_chrome.py/run_firefox.py.


how to run:
1-"python run_chrome.py" # for chrome
"python run_firefox.py" # for firefox
2- when web page successfuly loaded run "python httpserver.py"
3- send your local ip to victim and wait for it to get session
4- victim redirected automatically to real page
