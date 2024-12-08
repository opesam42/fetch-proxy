from flask import Blueprint, render_template
from main.get_proxy import scraper
import asyncio

bp = Blueprint("pages", __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/proxy')
def proxy():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    proxies = loop.run_until_complete(scraper()) 
    return render_template('proxy.html', proxies=proxies)