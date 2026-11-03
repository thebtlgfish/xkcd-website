import requests
import random

def get_latest():
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()
    data = response.json()
    latest_num = data["num"]
    return latest_num

def get_random_comic():
    latest = get_latest()
    num = random.randint(1, latest)
    r = requests.get(f"https://xkcd.com/{num}/info.0.json")
    data = r.json()
    link = f"https://xkcd.com/{num}"
    comic_num = data["num"]
    title = data["safe_title"]
    desc = data["alt"]
    img = data["img"]
    return link, comic_num, title, desc, img
    
