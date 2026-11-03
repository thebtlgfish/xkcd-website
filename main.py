from http_request import get_random_comic
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    link, comic_num, title, desc, img = get_random_comic()
    return render_template("index.html", link=link, comic_num=comic_num, title=title, desc=desc, img=img)
    


