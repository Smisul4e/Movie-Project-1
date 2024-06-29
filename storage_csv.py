import csv


class StorageCsv:
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        Format:
        {
          "title1": {
            "rating": rating1,
            "year": year1
          },
          "title2": {
            "rating": rating2,
            "year": year2
          },
          ...
        }
        """
        movies = {}
        try:
            with open(self.file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row.get('title', '')
                    rating = float(row.get('rating', 0.0))
                    year = int(row.get('year', 0))
                    if title:
                        movies[title] = {'rating': rating, 'year': year}
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
        except ValueError as e:
            print(f"Error: Failed to parse data in '{self.file_path}': {e}")
        except IOError as e:
            print(f"Error: Failed to read file '{self.file_path}': {e}")
        return movies

    def add_movie(self, title, year, rating):
        """
        Adds a new movie to the database.

        :param title: Title of the movie
        :param year: Release year of the movie
        :param rating: Rating of the movie
        """
        try:
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([title, year, rating])
        except IOError as e:
            print(f"Error: Failed to write to file '{self.file_path}': {e}")

    def update_movie(self, title, rating):
        """
        Updates the rating of an existing movie in the database.

        :param title: Title of the movie
        :param rating: New rating of the movie
        :return: True if update is successful; False otherwise
        """
        try:
            movies = self.list_movies()
            if title in movies:
                movies[title]['rating'] = rating
                self._save_movies(movies)
                return True
            else:
                print(f"Error: Movie '{title}' not found.")
        except IOError as e:
            print(f"Error: Failed to read or write to file '{self.file_path}': {e}")
        return False

    def delete_movie(self, title):
        """
        Deletes a movie from the database.

        :param title: Title of the movie to delete
        :return: True if the movie is deleted successfully; False otherwise
        """
        try:
            movies = self.list_movies()
            if title in movies:
                del movies[title]
                self._save_movies(movies)
                return True
            else:
                print(f"Error: Movie '{title}' not found.")
        except IOError as e:
            print(f"Error: Failed to read or write to file '{self.file_path}': {e}")
        return False

    def _save_movies(self, movies):
        """
        Saves the movies data back to the CSV file.

        :param movies: Dictionary containing movies data
        """
        try:
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'year', 'rating'])
                for title, info in movies.items():
                    writer.writerow([title, info['year'], info['rating']])
        except IOError as e:
            print(f"Error: Failed to write to file '{self.file_path}': {e}")
