from flask import render_template
from app import app 
from .request import get_news,get_articles

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    general_news = get_news('general')
    entertainment_news = get_news('entertainment')
    technology_news = get_news('technology')
    title = 'Home - Welcome to Prime News'
    return render_template('index.html', title = title,general = general_news,entertainment = entertainment_news,technology = technology_news)

@app.route('/news/<int:id>')
def articles(id):

    '''
    View articles page function that returns the  details page and its data
    '''
    articles =get_articles(id)
    title = f'{id}'

    return render_template('articles.html', articles=articles, title=title)