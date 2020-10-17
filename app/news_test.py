import unittest
from models import movie
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
       self.new_news= Sources(1235,'BBC News','https://www.bbc.com/news/entertainment-arts-54423918','Entertainment''USA', 'English' ) 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))


if __name__ == '__main__':
    unittest.main()