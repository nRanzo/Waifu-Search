# Project' Structure

waifu_search/
│
├── server.py
├── static/
│   └── index.html
└── templates/
    └── index.html

# Backend made with Flask

can be found in server.py, which is responsible to connect to waifu.im public api.

# Frontend made with HTML and Javascript

can be found in static/index.html, is responsible to properly display images.

# Instruction to run a vroom using venv:

unix based:
python3 -m venv venv
source venv/bin/activate

dos based:
python -m venv venv
venv\Scripts\activate

and then istall flask and requests if you have not already
pip install flask requests

only now you can run the Flask server by typing:
python server.py

and now you can open on your favourite web browser:
http://localhost:5000
