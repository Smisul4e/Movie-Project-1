import json

# Function to get movies from the JSON file
def get_movies():
    """Load movies from the JSON file."""
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save movies to the JSON file
def save_movies(movies):
    """Save movies to the JSON file."""
    with open('data.json', 'w') as file:
        json.dump(movies, file, indent=4)

# Function to add a movie to the JSON file
def add_movie(title, year, rating):
    """Add a movie to the JSON file."""
    movies = get_movies()
    movies[title] = {"year": year, "rating": rating}
    save_movies(movies)

# Function to delete a movie from the JSON file
def delete_movie(title):
    """Delete a movie from the JSON file."""
    movies = get_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)
        return True
    return False

# Function to update a movie's rating in the JSON file
def update_movie(title, rating):
    """Update a movie's rating in the JSON file."""
    movies = get_movies()
    if title in movies:
        movies[title]['rating'] = rating
        save_movies(movies)
        return True
    return False
