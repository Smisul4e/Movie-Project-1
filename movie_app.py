from colorama import Fore, init
from json_storage import StorageJson  # Importing StorageJson module


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def list_movies(self):
        movies = self._storage.list_movies()
        if not movies:
            print(Fore.YELLOW + "No movies found.")
        else:
            print(Fore.GREEN + f"Total movies: {len(movies)}")
            for title, details in movies.items():
                print(f"{title} ({details['year']}): {details['rating']}")

    def add_movie(self, title, year, rating):
        self._storage.add_movie(title, year, rating)
        print(Fore.GREEN + f"Movie '{title}' added successfully.")

    def delete_movie(self, title):
        if self._storage.delete_movie(title):
            print(Fore.GREEN + f"Movie '{title}' deleted successfully.")
        else:
            print(Fore.RED + f"Movie '{title}' not found.")

    def update_movie(self, title, rating):
        if self._storage.update_movie(title, rating):
            print(Fore.GREEN + f"Rating for movie '{title}' updated successfully.")
        else:
            print(Fore.RED + f"Movie '{title}' not found.")

    def run(self):
        init(autoreset=True)
        while True:
            print(Fore.CYAN + "********** Movie App **********")
            print(Fore.CYAN + "Menu:")
            print(Fore.CYAN + "1. List movies")
            print(Fore.CYAN + "2. Add movie")
            print(Fore.CYAN + "3. Delete movie")
            print(Fore.CYAN + "4. Update movie")
            print(Fore.CYAN + "5. Exit")

            choice = input(Fore.YELLOW + "Enter choice (1-5): ")

            if choice == '1':
                self.list_movies()
            elif choice == '2':
                title = input("Enter movie title: ")
                year = int(input("Enter release year: "))
                rating = float(input("Enter rating: "))
                self.add_movie(title, year, rating)
            elif choice == '3':
                title = input("Enter movie title to delete: ")
                self.delete_movie(title)
            elif choice == '4':
                title = input("Enter movie title to update: ")
                rating = float(input("Enter new rating: "))
                self.update_movie(title, rating)
            elif choice == '5':
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    storage_instance = StorageJson('movies.json')
    app = MovieApp(storage_instance)
    app.run()
