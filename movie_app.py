class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
        else:
            print(f"{len(movies)} movies in total")
            for title, details in movies.items():
                print(f"{title} ({details['year']}): {details['rating']}")

    def _command_movie_stats(self):
        movies = self._storage.list_movies()
        if not movies:
            print("No movies to display statistics.")
            return

        ratings = [details['rating'] for details in movies.values()]
        average = sum(ratings) / len(ratings)
        median = sorted(ratings)[len(ratings) // 2] if len(ratings) % 2 != 0 else \
            sum(sorted(ratings)[len(ratings) // 2 - 1:len(ratings) // 2 + 1]) / 2
        best_movies = [title for title, details in movies.items() if details['rating'] == max(ratings)]
        worst_movies = [title for title, details in movies.items() if details['rating'] == min(ratings)]

        print(f"Average rating: {average:.2f}")
        print(f"Median rating: {median:.2f}")
        print(f"Best movie(s): {', '.join(best_movies)}")
        print(f"Worst movie(s): {', '.join(worst_movies)}")

    def _command_add_movie(self):
        title = input("Enter the movie title: ")
        year = int(input("Enter the year of release: "))
        rating = float(input("Enter the movie rating: "))
        self._storage.add_movie(title, year, rating)
        print(f"Movie '{title}' added successfully.")

    def _command_delete_movie(self):
        title = input("Enter the movie title to delete: ")
        if self._storage.delete_movie(title):
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' not found.")

    def _command_update_movie(self):
        title = input("Enter the movie title to update: ")
        if title in self._storage.list_movies():
            rating = float(input("Enter the new rating: "))
            if self._storage.update_movie(title, rating):
                print(f"Movie '{title}' updated successfully.")
            else:
                print("Update failed.")
        else:
            print(f"Movie '{title}' not found.")

    def _generate_website(self):
        # Add implementation for generating a website here
        pass

    def run(self):
        while True:
            print("********** My Movies Database **********")
            print("Menu:")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Movie stats")
            print("6. Generate website")
            print("7. Exit")

            choice = input("Enter choice (1-7): ")

            if choice == '1':
                self._command_list_movies()
            elif choice == '2':
                self._command_add_movie()
            elif choice == '3':
                self._command_delete_movie()
            elif choice == '4':
                self._command_update_movie()
            elif choice == '5':
                self._command_movie_stats()
            elif choice == '6':
                self._generate_website()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")
