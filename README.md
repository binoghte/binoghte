- 👋 Hi, I’m @binoghte <br>
- 👀 I’m interested in hacking and programming<br>
- 📫 How to reach me mamad0761@gmail.com<br>
<br>
<br>
This is my first project on github<br>
Its a whatsapp qrljacker.<br>
It works with firefox and chrome.<br>
<br>
in firefox, session will not be saved .I'm looking for a good way to save it in next updates.<br>
in chrome you can set user-data-dir so the session remain if you close chrome. but for taking screen shot chrome will focus repeatly and it's annoying.<br>
<br>
how to it works:<br>
It runs a browser under selenium firefox/chrome(you need chrome driver compatible with your chrome version) and extract qrl code of web.whatsapp.com <br>
then runs an http server on port 80.just send your ip as a link to victim.<br>
index.html page in htdocs folder is a clone of web.whatsapp.com and repeadly reload qrl code that extracted and saved as htdocs/screenshot.png by run_chrome.py/run_firefox.py.<br>
<br>
<br>
how to run:<br>
1-"python run_chrome.py" # for chrome <br>
"python run_firefox.py" # for firefox<br>
2- when web page successfuly loaded run "python httpserver.py"<br>
3- send your local ip to victim and wait for it to get session<br>
4- victim redirected automatically to real page<br>
<br>
<br>
if you like this project and want more project<br>
please support me <br>
bitcoin wallet address : 18zkwpM7vX1cL1UuNvd5TvEm4UnCtfocoZ<br>
<br><br>
contact me : mamad0761@gmail.com<br>
