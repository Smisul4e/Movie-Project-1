import json


class StorageJson:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

    def list_movies(self):
        return self.data

    def add_movie(self, title, year, rating):
        if title in self.data:
            return False  # Movie already exists
        self.data[title] = {'year': year, 'rating': rating}
        self.save_data()
        return True

    def delete_movie(self, title):
        if title in self.data:
            del self.data[title]
            self.save_data()
            return True
        return False  # Movie not found

    def update_movie(self, title, rating):
        if title in self.data:
            self.data[title]['rating'] = rating
            self.save_data()
            return True
        return False  # Movie not found
