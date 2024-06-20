import random

# Dictionary to store the movies and the rating
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

def list_movies():
    print("\nList of movies:")
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")
    print()

def add_movie():
    movie = input("\nEnter the name of the movie: ")
    if movie in movies:
        print("Movie already exists.")
    else:
        try:
            rating = float(input("Enter the rating of the movie: "))
            movies[movie] = rating
            print(f"Movie '{movie}' added with rating {rating}.")
        except ValueError:
            print("Invalid rating. Please enter a numeric value.")
    print()

def delete_movie():
    movie = input("\nEnter the name of the movie to delete: ")
    if movie in movies:
        del movies[movie]
        print(f"Movie '{movie}' deleted.")
    else:
        print("Movie not found.")
    print()

def update_movie():
    movie = input("\nEnter the name of the movie to update: ")
    if movie in movies:
        try:
            rating = float(input("Enter the new rating of the movie: "))
            movies[movie] = rating
            print(f"Movie '{movie}' updated with new rating {rating}.")
        except ValueError:
            print("Invalid rating. Please enter a numeric value.")
    else:
        print("Movie not found.")
    print()

def stats():
    if not movies:
        print("\nNo movies in the database.")
        return

    highest_rated = max(movies, key=movies.get)
    lowest_rated = min(movies, key=movies.get)
    average_rating = sum(movies.values()) / len(movies)

    print("\nStatistics:")
    print(f"Highest rated movie: {highest_rated} with rating {movies[highest_rated]}")
    print(f"Lowest rated movie: {lowest_rated} with rating {movies[lowest_rated]}")
    print(f"Average movie rating: {average_rating:.1f}")
    print()

def random_movie():
    if not movies:
        print("\nNo movies in the database.")
        return

    movie = random.choice(list(movies.keys()))
    print(f"\nRandom movie: {movie} with rating {movies[movie]}")
    print()

def search_movie():
    query = input("\nEnter the name of the movie to search for: ")
    if query in movies:
        print(f"Found movie: {query} with rating {movies[query]}")
    else:
        print("Movie not found.")
    print()

def movies_sorted_by_rating():
    sorted_movies = sorted(movies.items(), key=lambda x: x[1], reverse=True)
    print("\nMovies sorted by rating:")
    for movie, rating in sorted_movies:
        print(f"{movie}: {rating}")
    print()
