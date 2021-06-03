import unittest
from ..models import movie
Movie=movie.Movie
class MovieTest(unittest.TestCase):
    '''
    Test case to test the behaviour of the movie class
    '''
    def setUp(self):
        '''
        set up test method that will run before each test
        '''
        self.new_movie=Movie(1234, 'python must be crazy', 'A thrilling new python series', 'https://image.tmdb.or/t/p/w500/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        '''
        test case to check if the self.new_movie is an instance of Movie class
        it uses the isinsatnce() function
        '''
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

    
       
if __name__=='__main__':
    unittest.main()
