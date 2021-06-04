
import os
class Config:
    '''
    general configuration parent class
    '''
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SECRET_KEY= os.environ.get('23a36')

class ProdConfig(Config):
    '''
    production configuration child class

    Arg:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}
