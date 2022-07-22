from unittest.mock import Mock
from flask import request
import tmdb_client

def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']
   
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list


# test pobierania danych z API TheMovieDB
def test_get_single_movie1():
   movie = tmdb_client.get_single_movie(movie_id=616037)
   assert movie is not None

# test pobierania danych z API TheMovieDB - metoda request.get
def test_get_single_movie2(monkeypatch):
   mock_movie = '616037'
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie = tmdb_client.get_single_movie(movie_id='616037')
   assert movie == mock_movie


# test pobierania danych z API TheMovieDB - metoda request.get
def test_get_movie_images(monkeypatch):
   mock_image = ['test.jpg']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_image
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   image = tmdb_client.get_movie_images(movie_id='616037')
   assert image == mock_image

def test_get_single_movie_cast(monkeypatch):
   mock_cast = {'cast':[{'name': 'Gemma Chan'}]}
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   test_cast = tmdb_client.get_single_movie_cast(movie_id='616037')
   assert test_cast == mock_cast['cast']