import json
from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def get_movies(self):
        pass

    @abstractmethod
    def save_movies(self, movies):
        pass

    @abstractmethod
    def add_movie(self, title, year, rating):
        pass

    @abstractmethod
    def delete_movie(self, title):
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        pass


class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_movies(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_movies(self, movies):
        with open(self.filename, 'w') as file:
            json.dump(movies, file, indent=4)

    def add_movie(self, title, year, rating):
        movies = self.get_movies()
        movies[title] = {"year": year, "rating": rating}
        self.save_movies(movies)

    def delete_movie(self, title):
        movies = self.get_movies()
        if title in movies:
            del movies[title]
            self.save_movies(movies)
            return True
        return False

    def update_movie(self, title, rating):
        movies = self.get_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self.save_movies(movies)
            return True
        return False
