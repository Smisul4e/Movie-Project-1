import random
import statistics
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from colorama import Fore, Style, init

# Инициализиране на colorama
init(autoreset=True)

def list_movies(movies):
    print(Fore.CYAN + f"{len(movies)} movies in total")
    for movie, details in movies.items():
        print(f"{movie} ({details['year']}): {details['rating']}")

def add_movie(movies):
    name = input(Fore.YELLOW + "Enter movie name: ")
    rating = float(input(Fore.YELLOW + "Enter movie rating: "))
    year = int(input(Fore.YELLOW + "Enter year of release: "))
    movies[name] = {"rating": rating, "year": year}
    print(Fore.GREEN + f"Movie '{name}' added with rating {rating} and year {year}")

def delete_movie(movies):
    name = input(Fore.YELLOW + "Enter movie name to delete: ")
    if name in movies:
        del movies[name]
        print(Fore.GREEN + f"Movie '{name}' deleted")
    else:
        print(Fore.RED + f"Error: Movie '{name}' not found")

def update_movie(movies):
    name = input(Fore.YELLOW + "Enter movie name to update: ")
    if name in movies:
        rating = float(input(Fore.YELLOW + "Enter new rating: "))
        movies[name]['rating'] = rating
        print(Fore.GREEN + f"Movie '{name}' updated with new rating {rating}")
    else:
        print(Fore.RED + f"Error: Movie '{name}' not found")

def stats(movies):
    if not movies:
        print(Fore.RED + "No movies in the database")
        return
    ratings = [details['rating'] for details in movies.values()]
    average = statistics.mean(ratings)
    median = statistics.median(ratings)
    best_movies = [name for name, details in movies.items() if details['rating'] == max(ratings)]
    worst_movies = [name for name, details in movies.items() if details['rating'] == min(ratings)]
    print(Fore.CYAN + f"Average rating: {average}")
    print(Fore.CYAN + f"Median rating: {median}")
    print(Fore.CYAN + f"Best movie(s): {', '.join(best_movies)}")
    print(Fore.CYAN + f"Worst movie(s): {', '.join(worst_movies)}")

def random_movie(movies):
    if not movies:
        print(Fore.RED + "No movies in the database")
        return
    name, details = random.choice(list(movies.items()))
    print(Fore.CYAN + f"Random movie: {name} ({details['year']}) with rating {details['rating']}")

def search_movie(movies):
    part = input(Fore.YELLOW + "Enter part of movie name: ").lower()
    found_movies = {name: details for name, details in movies.items() if part in name.lower()}
    if found_movies:
        for movie, details in found_movies.items():
            print(f"{movie} ({details['year']}): {details['rating']}")
    else:
        similar_movies = process.extract(part, movies.keys(), scorer=fuzz.partial_ratio)
        if similar_movies:
            print(Fore.RED + f'The movie "{part}" does not exist. Did you mean:')
            for movie, score in similar_movies:
                if score > 70:  # Adjust this threshold based on your preference
                    print(f"{movie}")
        else:
            print(Fore.RED + f'No similar movies found for "{part}"')

def movies_sorted_by_rating(movies):
    sorted_movies = sorted(movies.items(), key=lambda item: item[1]['rating'], reverse=True)
    for movie, details in sorted_movies:
        print(f"{movie} ({details['year']}): {details['rating']}")

def create_rating_histogram(movies):
    if not movies:
        print(Fore.RED + "No movies in the database")
        return
    ratings = [details['rating'] for details in movies.values()]
    plt.hist(ratings, bins=10, edgecolor='black')
    plt.title('Movie Ratings Histogram')
    plt.xlabel('Rating')
    plt.ylabel('Number of Movies')
    filename = input(Fore.YELLOW + "Enter filename to save the histogram (e.g., histogram.png): ")
    plt.savefig(filename)
    plt.close()
    print(Fore.GREEN + f"Histogram saved to {filename}")

def main():
    movies = {
        "The Shawshank Redemption": {"rating": 9.5, "year": 1994},
        "Pulp Fiction": {"rating": 8.8, "year": 1994},
        "The Room": {"rating": 3.6, "year": 2003},
        "The Godfather": {"rating": 9.2, "year": 1972},
        "The Godfather: Part II": {"rating": 9.0, "year": 1974},
        "The Dark Knight": {"rating": 9.0, "year": 2008},
        "12 Angry Men": {"rating": 8.9, "year": 1957},
        "Everything Everywhere All At Once": {"rating": 8.9, "year": 2022},
        "Forrest Gump": {"rating": 8.8, "year": 1994},
        "Star Wars: Episode V": {"rating": 8.7, "year": 1980}
    }

    while True:
        print(Fore.MAGENTA + "\n********** My Movies Database **********")
        print(Fore.BLUE + "Menu:")
        print(Fore.BLUE + "1. List movies")
        print(Fore.BLUE + "2. Add movie")
        print(Fore.BLUE + "3. Delete movie")
        print(Fore.BLUE + "4. Update movie")
        print(Fore.BLUE + "5. Stats")
        print(Fore.BLUE + "6. Random movie")
        print(Fore.BLUE + "7. Search movie")
        print(Fore.BLUE + "8. Movies sorted by rating")
        print(Fore.BLUE + "9. Create Rating Histogram")
        print(Fore.BLUE + "10. Exit")
        choice = input(Fore.YELLOW + "Enter choice (1-10): ")

        if choice == "1":
            list_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            update_movie(movies)
        elif choice == "5":
            stats(movies)
        elif choice == "6":
            random_movie(movies)
        elif choice == "7":
            search_movie(movies)
        elif choice == "8":
            movies_sorted_by_rating(movies)
        elif choice == "9":
            create_rating_histogram(movies)
        elif choice == "10":
            print(Fore.GREEN + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice, please try again")

if __name__ == "__main__":
    main()
