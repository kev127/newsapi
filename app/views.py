from flask import render_template
from app import app 
from .request import get_sources,get_articles

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''  
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    health_sources = get_sources('health')
    science_sources = get_sources('science')
    title = 'Home - Welcome to Prime News'
    return render_template('index.html',title=title,business = business_sources,health=health_sources,science=science_sources,sports = sports_sources, technology = technology_sources,entertainment = entertainment_sources ,general=general_sources)

@app.route('/news/<int:id>')
def articles(id):

    '''
    View articles page function that returns the  details page and its data
    '''
    articles =get_articles(id)
    title = f'{id}'

    return render_template('articles.html', articles=articles, title=title)