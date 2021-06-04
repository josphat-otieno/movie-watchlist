import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.or/t/p/w500/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

    def test_init(self):
        '''
        test case to confirm the movie object is instantiated correctly
        '''
        self.assertEqual(self.new_movie.id,1234)
        self.assertEqual(self.new_movie.title,'python must be crazy')
        self.assertEqual(self.new_movie.overview,'A thrilling new python series')
        self.assertEqual(self.new_movie.poster,'https://image.tmdb.or/t/p/w500/w500/khsjha27hbs')
        self.assertEqual(self.new_movie.vote_average,8.5)
        self.assertEqual(self.new_movie.vote_count,129993 )

