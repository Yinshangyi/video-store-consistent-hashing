from typing import List

import requests


def clean_movie_title(title: str) -> str:
    return title \
        .replace(" ", "-") \
        .replace(":", "") \
        .replace("\n", "") \
        + ".mp4"


def get_movies_list() -> List[str]:
    with open("movies.txt", "r") as file:
        raw_movies = file.readlines()
        clean_movies = [clean_movie_title(movie) for movie in raw_movies]
    return clean_movies


def post_movie(title: str):
    requests.post(f"http://localhost:5000/video/{title}")


movies = get_movies_list()
for movie in movies:
    post_movie(movie)
