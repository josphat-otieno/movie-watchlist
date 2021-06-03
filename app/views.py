from .request import get_movies, get_movie
from flask import render_template
from app import app
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    popular_movies=get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    print(popular_movies)
    title="Home- welcome to the best movie review website online"
    message ='Welcome to movie database'
    return render_template('index.html', title=title, message=message,popular=popular_movies,upcoming=upcoming_movie,now_playing=now_showing_movie)

# @app.route('/movie/<int:movie_id>')
# def movie(movie_id):
#     '''
#     view movie page function that returns the movie details page and its data
#     '''
    # getting popular movies
    
    # title = f'you are viewing movie {movie_id}'
    # return render_template('movie.html', title=title, )

@app.route('/movie/<int:id>')
def movie(id):
    '''
    view movie page function tht returns the movie details page and its data
    '''
    movie=get_movie(id)
    title=f'{movie.title}'

    return render_template('movie.html', title=title, movie=movie)

