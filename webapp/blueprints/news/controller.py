from flask import Blueprint, render_template

news = Blueprint('news', __name__,
                 template_folder='views', url_prefix="/news")


@news.route('/')
def news_home():
    return render_template('index.html')


@news.route('/pricing')
def news_pricing():
    return render_template('pricing.html')
