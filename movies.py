import random
import matplotlib.pyplot as plt
from fuzzywuzzy import process
from colorama import Fore, init
from movie_app import MovieApp
from json_storage import StorageJson

def list_movies(movie_app):
    movies = movie_app.list_movies()
    if not movies:
        print(Fore.GREEN + "No movies found in the database.")
    else:
        print(Fore.MAGENTA + f"{len(movies)} movies in total")
        for title, details in movies.items():
            print(f"{title} ({details['year']}): {details['rating']}")

def add_movie(movie_app):
    movies = movie_app.list_movies()
    title = input("Enter the movie title: ")
    if title in movies:
        print(Fore.MAGENTA + f"Movie '{title}' already exists!")
        return
    rating = float(input("Enter the movie rating: "))
    year = int(input("Enter the year of release: "))
    movie_app.add_movie(title, year, rating)
    print(Fore.GREEN + f"Movie '{title}' added successfully.")

def delete_movie(movie_app):
    title = input("Enter the movie title to delete: ")
    if movie_app.delete_movie(title):
        print(Fore.GREEN + f"Movie '{title}' deleted successfully.")
    else:
        print(Fore.MAGENTA + f"Movie '{title}' not found in the database.")

def update_movie(movie_app):
    title = input("Enter the movie title to update: ")
    if title in movie_app.list_movies():
        rating = float(input("Enter the new rating: "))
        if movie_app.update_movie(title, rating):
            print(Fore.GREEN + f"Movie '{title}' updated successfully.")
        else:
            print(Fore.MAGENTA + "Update failed.")
    else:
        print(Fore.MAGENTA + f"Movie '{title}' not found in the database.")

def display_stats(movie_app):
    movies = movie_app.list_movies()
    if not movies:
        print(Fore.GREEN + "No movies to display statistics.")
        return

    ratings = [details['rating'] for details in movies.values()]
    average = sum(ratings) / len(ratings)
    median = sorted(ratings)[len(ratings) // 2] if len(ratings) % 2 != 0 else \
        sum(sorted(ratings)[len(ratings) // 2 - 1:len(ratings) // 2 + 1]) / 2
    best_movies = [title for title, details in movies.items() if details['rating'] == max(ratings)]
    worst_movies = [title for title, details in movies.items() if details['rating'] == min(ratings)]

    print(Fore.GREEN + f"Average rating: {average:.2f}")
    print(Fore.GREEN + f"Median rating: {median:.2f}")
    print(Fore.GREEN + f"Best movie(s): {', '.join(best_movies)}")
    print(Fore.GREEN + f"Worst movie(s): {', '.join(worst_movies)}")

def create_histogram(movie_app):
    movies = movie_app.list_movies()
    ratings = [details['rating'] for details in movies.values()]
    plt.hist(ratings, bins=10, edgecolor='black')
    plt.xlabel('Ratings')
    plt.ylabel('Number of Movies')
    plt.title('Movie Ratings Histogram')
    filename = input("Enter the filename to save the histogram: ")
    plt.savefig(filename)
    print(Fore.GREEN + f"Histogram saved to {filename}")

def search_movie(movie_app):
    movies = movie_app.list_movies()
    query = input("Enter part of the movie name: ")
    matches = [title for title in movies if process.extractOne(query.lower(), [title.lower()])[1] >= 80]

    if matches:
        print(Fore.GREEN + "Found movies:")
        for match in matches:
            print(f"{match}: {movies[match]['rating']}")
    else:
        print(Fore.MAGENTA + f"No exact match for '{query}' found.")
        suggestions = process.extract(query, movies.keys(), limit=5)
        if suggestions:
            print(Fore.GREEN + "Did you mean:")
            for suggestion, score in suggestions:
                if score > 60:
                    print(f"{suggestion} ({movies[suggestion]['year']}): {movies[suggestion]['rating']}")

def random_movie(movie_app):
    movies = movie_app.list_movies()
    if not movies:
        print(Fore.GREEN + "No movies found in the database.")
    else:
        title = random.choice(list(movies.keys()))
        print(Fore.MAGENTA + f"Random movie: {title} ({movies[title]['year']}): {movies[title]['rating']}")

def filter_movies(movie_app):
    """Filter movies based on user criteria"""
    min_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
    start_year = input("Enter start year (leave blank for no start year): ")
    end_year = input("Enter end year (leave blank for no end year): ")

    movies = movie_app.list_movies()

    # Convert inputs to proper types if they are not blank
    min_rating = float(min_rating) if min_rating else None
    start_year = int(start_year) if start_year else None
    end_year = int(end_year) if end_year else None

    filtered_movies = {}
    for title, details in movies.items():
        if (min_rating is None or details['rating'] >= min_rating) and \
           (start_year is None or details['year'] >= start_year) and \
           (end_year is None or details['year'] <= end_year):
            filtered_movies[title] = details

    if not filtered_movies:
        print(Fore.MAGENTA + "No movies found matching the criteria.")
    else:
        print(Fore.GREEN + "Filtered Movies:")
        for title, details in filtered_movies.items():
            print(f"{title} ({details['year']}): {details['rating']}")

def main():
    init(autoreset=True)
    storage = StorageJson('movies.json')
    movie_app = MovieApp(storage)

    while True:
        print(Fore.CYAN + "********** My Movies Database **********")
        print(Fore.CYAN + "Menu:")
        print(Fore.CYAN + "1. List movies")
        print(Fore.CYAN + "2. Add movie")
        print(Fore.CYAN + "3. Delete movie")
        print(Fore.CYAN + "4. Update movie")
        print(Fore.CYAN + "5. Stats")
        print(Fore.CYAN + "6. Random movie")
        print(Fore.CYAN + "7. Search movie")
        print(Fore.CYAN + "8. Movies sorted by rating")
        print(Fore.CYAN + "9. Create Rating Histogram")
        print(Fore.CYAN + "10. Filter movies")
        print(Fore.CYAN + "11. Movies sorted by year")
        print(Fore.CYAN + "12. Exit")

        choice = input(Fore.YELLOW + "Enter choice (1-12): ")

        if choice == '1':
            list_movies(movie_app)
        elif choice == '2':
            add_movie(movie_app)
        elif choice == '3':
            delete_movie(movie_app)
        elif choice == '4':
            update_movie(movie_app)
        elif choice == '5':
            display_stats(movie_app)
        elif choice == '6':
            random_movie(movie_app)
        elif choice == '7':
            search_movie(movie_app)
        elif choice == '8':
            sorted_movies = movie_app.sorted_movies_by_rating()
            for title, details in sorted_movies:
                print(f"{title} ({details['year']}): {details['rating']}")
        elif choice == '9':
            create_histogram(movie_app)
        elif choice == '10':
            filter_movies(movie_app)
        elif choice == '11':
            order = input("Do you want to see the latest movies first? (yes/no): ").strip().lower()
            sorted_movies = movie_app.sorted_movies_by_year(order)
            for title, details in sorted_movies:
                print(f"{title} ({details['year']}): {details['rating']}")
        elif choice == '12':
            break
        else:
            print(Fore.MAGENTA + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
