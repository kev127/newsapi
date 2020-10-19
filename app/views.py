from flask import render_template
from app import app 
from .request import get_sources,get_articles
from .models import source

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''  
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    health_sources = get_sources('health')
    title = 'Home - Welcome to Prime News'
    return render_template('index.html',title=title,business_sources=business_sources,sports_sources=sports_sources,technology_sources=technology_sources,entertainment_sources=entertainment_sources)

@app.route('/news/<int:id>')
def articles(id):

    '''
    View articles page function that returns the  details page and its data
    '''
    articles =get_articles(id)
    title = f'{id}'

    return render_template('articles.html', articles=articles, title=title)