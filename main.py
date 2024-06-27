import random
import statistics


def list_movies(movies):
    print(f"{len(movies)} movies in total")
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def add_movie(movies):
    name = input("Enter movie name: ")
    rating = float(input("Enter movie rating: "))
    movies[name] = rating
    print(f"Movie '{name}' added with rating {rating}")


def delete_movie(movies):
    name = input("Enter movie name to delete: ")
    if name in movies:
        del movies[name]
        print(f"Movie '{name}' deleted")
    else:
        print(f"Error: Movie '{name}' not found")


def update_movie(movies):
    name = input("Enter movie name to update: ")
    if name in movies:
        rating = float(input("Enter new rating: "))
        movies[name] = rating
        print(f"Movie '{name}' updated with new rating {rating}")
    else:
        print(f"Error: Movie '{name}' not found")


def stats(movies):
    if not movies:
        print("No movies in the database")
        return
    ratings = list(movies.values())
    average = statistics.mean(ratings)
    median = statistics.median(ratings)
    best_movies = [name for name, rating in movies.items() if rating == max(ratings)]
    worst_movies = [name for name, rating in movies.items() if rating == min(ratings)]
    print(f"Average rating: {average}")
    print(f"Median rating: {median}")
    print(f"Best movie(s): {', '.join(best_movies)}")
    print(f"Worst movie(s): {', '.join(worst_movies)}")


def random_movie(movies):
    if not movies:
        print("No movies in the database")
        return
    name, rating = random.choice(list(movies.items()))
    print(f"Random movie: {name} with rating {rating}")


def search_movie(movies):
    part = input("Enter part of movie name: ").lower()
    found_movies = {name: rating for name, rating in movies.items() if part in name.lower()}
    if found_movies:
        for movie, rating in found_movies.items():
            print(f"{movie}: {rating}")
    else:
        print("No movies found")


def movies_sorted_by_rating(movies):
    sorted_movies = sorted(movies.items(), key=lambda item: item[1], reverse=True)
    for movie, rating in sorted_movies:
        print(f"{movie}: {rating}")


def main():
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    while True:
        print("\n********** My Movies Database **********")
        print("Menu:")
        print("1. List movies")
        print("2. Add movie")
        print("3. Delete movie")
        print("4. Update movie")
        print("5. Stats")
        print("6. Random movie")
        print("7. Search movie")
        print("8. Movies sorted by rating")
        print("9. Exit")
        choice = input("Enter choice (1-9): ")

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
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
