# Want to support this project? leave a star!

Scroll to the bottom to see version updates and patch releases

# Project' structure - version 1.1

    waifu_search/
    │
    ├── server.py
    ├── static/
    │   └── 
    └── templates/
        └── index.html

# Backend made with Flask

is responsible to connect to waifu.im public api and send links to the frontend - it can be found in server.py

# Frontend made with HTML and Javascript

is responsible to receive you messages and to display images - it can be found in template/index.html

# Instruction to run a vroom using venv:

unix-based systems:
python3 -m venv venv
source venv/bin/activate

dos-based systems:
python -m venv venv
venv\Scripts\activate

and then istall flask and requests if you have not already
pip install flask requests

only now you can run the Flask server by typing:
python server.py

and now you can open on your favourite web browser:
http://localhost:5000

# version 1.0 ---- Please read
Currently the index.html is unable to reveive any links from server.py and image can't be seen from index.html file.

# version 1.1 ---- Please read
Currently the index.html receives all the needed links from server.py, but it's unable to display any image correctly.
Also note that some prompt cause request failure 404, so for any test please write only "waifu" and send the message.
