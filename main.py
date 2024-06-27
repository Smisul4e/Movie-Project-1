import movie_storage
import matplotlib.pyplot as plt
from fuzzywuzzy import process
from colorama import Fore, init
import random


def list_movies():
    movies = movie_storage.get_movies()
    if not movies:
        print(Fore.YELLOW + "No movies found in the database.")
    else:
        print(Fore.LIGHTGREEN_EX + f"{len(movies)} movies in total")
        for title, details in movies.items():
            print(f"{title} ({details['year']}): {details['rating']}")


def add_movie():
    movies = movie_storage.get_movies()
    title = input("Enter the movie title: ")
    if title in movies:
        print(Fore.LIGHTRED_EX + f"Movie '{title}' already exists!")
        return
    rating = float(input("Enter the movie rating: "))
    year = int(input("Enter the year of release: "))
    movie_storage.add_movie(title, year, rating)
    print(Fore.LIGHTGREEN_EX + f"Movie '{title}' added successfully.")


def delete_movie():
    title = input("Enter the movie title to delete: ")
    if movie_storage.delete_movie(title):
        print(Fore.LIGHTGREEN_EX + f"Movie '{title}' deleted successfully.")
    else:
        print(Fore.LIGHTRED_EX + f"Movie '{title}' not found in the database.")


def update_movie():
    title = input("Enter the movie title to update: ")
    if title in movie_storage.get_movies():
        rating = float(input("Enter the new rating: "))
        if movie_storage.update_movie(title, rating):
            print(Fore.LIGHTGREEN_EX + f"Movie '{title}' updated successfully.")
        else:
            print(Fore.LIGHTRED_EX + "Update failed.")
    else:
        print(Fore.LIGHTRED_EX + f"Movie '{title}' not found in the database.")


def display_stats():
    movies = movie_storage.get_movies()
    if not movies:
        print(Fore.YELLOW + "No movies to display statistics.")
        return

    ratings = [details['rating'] for details in movies.values()]
    average = sum(ratings) / len(ratings)
    median = sorted(ratings)[len(ratings) // 2] if len(ratings) % 2 != 0 else \
        sum(sorted(ratings)[len(ratings) // 2 - 1:len(ratings) // 2 + 1]) / 2
    best_movies = [title for title, details in movies.items() if details['rating'] == max(ratings)]
    worst_movies = [title for title, details in movies.items() if details['rating'] == min(ratings)]

    print(Fore.LIGHTGREEN_EX + f"Average rating: {average:.2f}")
    print(Fore.LIGHTGREEN_EX + f"Median rating: {median:.2f}")
    print(Fore.LIGHTGREEN_EX + f"Best movie(s): {', '.join(best_movies)}")
    print(Fore.LIGHTGREEN_EX + f"Worst movie(s): {', '.join(worst_movies)}")


def create_histogram():
    movies = movie_storage.get_movies()
    ratings = [details['rating'] for details in movies.values()]
    plt.hist(ratings, bins=10, edgecolor='black')
    plt.xlabel('Ratings')
    plt.ylabel('Number of Movies')
    plt.title('Movie Ratings Histogram')
    filename = input("Enter the filename to save the histogram: ")
    plt.savefig(filename)
    print(Fore.LIGHTGREEN_EX + f"Histogram saved to {filename}")


def search_movie():
    movies = movie_storage.get_movies()
    query = input("Enter part of the movie name: ")
    matches = [title for title in movies if process.extractOne(query.lower(), [title.lower()])[1] >= 80]

    if matches:
        print(Fore.LIGHTGREEN_EX + "Found movies:")
        for match in matches:
            print(f"{match}: {movies[match]['rating']}")
    else:
        print(Fore.LIGHTRED_EX + f"No exact match for '{query}' found.")
        suggestions = process.extract(query, movies.keys(), limit=5)
        if suggestions:
            print(Fore.YELLOW + "Did you mean:")
            for suggestion, score in suggestions:
                if score > 60:
                    print(f"{suggestion} ({movies[suggestion]['year']}): {movies[suggestion]['rating']}")


def random_movie():
    movies = movie_storage.get_movies()
    if not movies:
        print(Fore.YELLOW + "No movies found in the database.")
    else:
        title = random.choice(list(movies.keys()))
        print(Fore.LIGHTGREEN_EX + f"Random movie: {title} ({movies[title]['year']}): {movies[title]['rating']}")


def list_movies_by_year():
    movies = movie_storage.get_movies()
    if not movies:
        print(Fore.YELLOW + "No movies found in the database.")
        return

    choice = input("Do you want to see the latest movies first? (y/n): ").lower()
    reverse_order = choice == 'y'

    sorted_movies = sorted(movies.items(), key=lambda item: item[1]['year'], reverse=reverse_order)
    for title, details in sorted_movies:
        print(f"{title} ({details['year']}): {details['rating']}")


def main():
    init(autoreset=True)
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
        print(Fore.CYAN + "9. Movies sorted by year")
        print(Fore.CYAN + "10. Create Rating Histogram")
        print(Fore.CYAN + "11. Exit")

        choice = input(Fore.LIGHTYELLOW_EX + "Enter choice (1-11): ")

        if choice == '1':
            list_movies()
        elif choice == '2':
            add_movie()
        elif choice == '3':
            delete_movie()
        elif choice == '4':
            update_movie()
        elif choice == '5':
            display_stats()
        elif choice == '6':
            random_movie()
        elif choice == '7':
            search_movie()
        elif choice == '8':
            sorted_movies = sorted(movie_storage.get_movies().items(), key=lambda item: item[1]['rating'], reverse=True)
            for title, details in sorted_movies:
                print(f"{title} ({details['year']}): {details['rating']}")
        elif choice == '9':
            list_movies_by_year()
        elif choice == '10':
            create_histogram()
        elif choice == '11':
            break
        else:
            print(Fore.LIGHTRED_EX + "Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
