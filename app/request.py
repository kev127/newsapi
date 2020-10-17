from app import app
import urllib.request,json
from .models import news, Articles

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

# Getting the articles base url
articles_base_url = app.config['ARTICLES_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')
        language = news_item.get('language')

            news_object = news(id,name,description,url,category,country,language)
            news_results.append(news_object)

    return movie_results    

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(articles_list):
    '''
     Function that processes the news articles results and turns them into a list of objects
     Args:
             articles_list: A list of dictionaries that contain sources details
     Returns:
             articles_results: A list of sources objects
     '''
    articles_results = []

    for articles_item in articles_list:
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        
        articles_object = Articles(
            title, description, url, urlToImage, publishedAt)
        articles_results.append(articles_object)


    return articles_results
