# istorage.py

from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster_url):
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        pass

    @abstractmethod
    def delete_movie(self, title):
        pass
