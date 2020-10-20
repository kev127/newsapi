import unittest
from .models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources= Sources(1235,'BBC News','https://www.bbc.co.uk/news/technology-54148474','Business','USA', 'English' ) 

    def test_instance(self):
        '''
        Test to check creation of new article Sources instance
        '''
        self.assertTrue(isinstance(self.new_source,Source))