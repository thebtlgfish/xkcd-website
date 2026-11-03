from flask import Flask, render_template
from http_request import get_random_comic

# Since templates is now inside the API folder, Flask finds it automatically!
app = Flask(__name__)

@app.route("/")
def home():
    try:
        link, comic_num, title, desc, img = get_random_comic()
        return render_template(
            "index.html", 
            link=link, 
            comic_num=comic_num, 
            title=title, 
            desc=desc, 
            img=img
        )
    except Exception as e:
        # This will show the exact error on your page so you can see what failed
        return f"<h3>Application Error:</h3><pre>{str(e)}</pre>", 500
