from flask import Flask
import requests
import random

import os
API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")
print("=============> ", API_TOKEN)

app = Flask(__name__)
app.config["SECRET_KEY"] = 'alamakota'

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
    response = requests.get(endpoint_2, headers=headers)
    return response.json()

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")

#def get_movies_list(list_type):
#    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
#    headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#    }
#    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
#    response = requests.get(endpoint_2, headers=headers)
#    response.raise_for_status()
#    return response.json()

def get_poster_urls(poster_api_path, size):
    tmdb_url = "https://image.tmdb.org/t/p/"
    poster_url = f"{tmdb_url}{size}{poster_api_path}"
    return poster_url

#def get_movies(how_many, list_type='popular'):
#    data = get_popular_movies()
#    random.shuffle(data['results'])
#    return data["results"][:how_many]

def get_movies(list_type, how_many):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
    response = requests.get(endpoint_2, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
    response = requests.get(endpoint_2, headers=headers)
    return response.json()["cast"]

def get_cast(movie_id, how_many=8):
    data = get_single_movie_cast(movie_id)
    return data[:how_many]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
    response = requests.get(endpoint_2, headers=headers)
    return response.json()

def search(search_query):
   endpoint = f"https://api.themoviedb.org/3/search/movie/?query={search_query}"
   
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   
   response = requests.get(endpoint, headers=headers)
   response = response.json()
   return response['results']

def get_airing_today():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']
