from flask import Blueprint, render_template
from main.get_proxy import scraper
import asyncio

bp = Blueprint("pages", __name__)

@bp.route('/')
def home():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    proxies = loop.run_until_complete(scraper()) 

    return render_template('home.html', proxies=proxies)

@bp.route('/about')
def about():
    return "about page"