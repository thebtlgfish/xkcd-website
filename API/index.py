from flask import Flask, render_template
from http_request import get_random_comic

# Vercel looks for this 'app' variable via your pyproject.toml entrypoint
app = Flask(__name__, template_folder='../templates')

@app.route("/")
def home():
    # Unpack the 5 values returned by your http_request.py function
    link, comic_num, title, desc, img = get_random_comic()
    
    return render_template(
        "index.html", 
        link=link, 
        comic_num=comic_num, 
        title=title, 
        desc=desc, 
        img=img
    )
