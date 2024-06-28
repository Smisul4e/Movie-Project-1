class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def list_movies(self):
        return self._storage.list_movies()

    def add_movie(self, title, year, rating):
        return self._storage.add_movie(title, year, rating)

    def delete_movie(self, title):
        return self._storage.delete_movie(title)

    def update_movie(self, title, rating):
        return self._storage.update_movie(title, rating)

    def display_stats(self):
        return self._storage.display_stats()

    def create_histogram(self):
        return self._storage.create_histogram()

    def search_movie(self, query):
        return self._storage.search_movie(query)

    def random_movie(self):
        return self._storage.random_movie()

    def filter_movies(self, min_rating=None, start_year=None, end_year=None):
        return self._storage.filter_movies(min_rating, start_year, end_year)

    def sorted_movies_by_rating(self):
        return sorted(self._storage.list_movies().items(), key=lambda item: item[1]['rating'], reverse=True)

    def sorted_movies_by_year(self, order):
        return sorted(self._storage.list_movies().items(), key=lambda item: item[1]['year'], reverse=(order == 'yes'))
