import random
import statistics
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from colorama import Fore, Style, init
import json
import os

FILE_PATH = 'movies.json'

# Initialize colorama
init(autoreset=True)

def load_movies_from_file():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_movies_to_file(movies):
    with open(FILE_PATH, 'w') as file:
        json.dump(movies, file, indent=4)

movies = load_movies_from_file()

def list_movies():
    if not movies:
        print(f"{Fore.RED}No movies found in the database.{Style.RESET_ALL}")
    else:
        print(f"{Fore.BLUE}{len(movies)} movies in total{Style.RESET_ALL}")
        for title, info in movies.items():
            print(f"{title}: {info['rating']} (Year: {info['year']})")

def add_movie():
    title = input("Enter movie title: ").strip()
    if title in movies:
        print(f"{Fore.RED}The movie '{title}' already exists in the database.{Style.RESET_ALL}")
        return
    rating = float(input("Enter movie rating: ").strip())
    year = int(input("Enter movie release year: ").strip())
    movies[title] = {'rating': rating, 'year': year}
    save_movies_to_file(movies)
    print(f"{Fore.GREEN}Movie '{title}' added successfully!{Style.RESET_ALL}")

def delete_movie():
    title = input("Enter movie title to delete: ").strip()
    if title not in movies:
        print(f"{Fore.RED}The movie '{title}' does not exist in the database.{Style.RESET_ALL}")
        return
    del movies[title]
    save_movies_to_file(movies)
    print(f"{Fore.GREEN}Movie '{title}' deleted successfully!{Style.RESET_ALL}")

def update_movie():
    title = input("Enter movie title to update: ").strip()
    if title not in movies:
        print(f"{Fore.RED}The movie '{title}' does not exist in the database.{Style.RESET_ALL}")
        return
    rating = float(input("Enter new movie rating: ").strip())
    movies[title]['rating'] = rating
    save_movies_to_file(movies)
    print(f"{Fore.GREEN}Movie '{title}' updated successfully!{Style.RESET_ALL}")

def create_rating_histogram():
    ratings = [info['rating'] for info in movies.values()]
    plt.hist(ratings, bins=10, edgecolor='black')
    plt.xlabel('Rating')
    plt.ylabel('Number of Movies')
    plt.title('Movies Rating Histogram')
    file_name = input("Enter the filename to save the histogram (e.g., histogram.png): ").strip()
    plt.savefig(file_name)
    print(f"{Fore.GREEN}Histogram saved as {file_name}{Style.RESET_ALL}")

def search_movie():
    query = input("Enter part of movie name: ").strip().lower()
    results = [title for title in movies if query in title.lower()]
    if results:
        for title in results:
            print(f"{title}: {movies[title]['rating']} (Year: {movies[title]['year']})")
    else:
        print(f"{Fore.RED}No direct match found for '{query}'. Searching for similar titles...{Style.RESET_ALL}")
        suggestions = process.extract(query, movies.keys(), limit=3)
        for suggestion in suggestions:
            title, score = suggestion
            print(f"Did you mean: {title}? (Rating: {movies[title]['rating']}, Year: {movies[title]['year']})")

def main():
    while True:
        print(f"""
        {Fore.YELLOW}********** My Movies Database **********{Style.RESET_ALL}
        Menu:
        1. List movies
        2. Add movie
        3. Delete movie
        4. Update movie
        5. Stats
        6. Random movie
        7. Search movie
        8. Movies sorted by rating
        9. Create Rating Histogram
        10. Exit
        """)
        choice = input("Enter choice (1-10): ").strip()
        if choice == '1':
            list_movies()
        elif choice == '2':
            add_movie()
        elif choice == '3':
            delete_movie()
        elif choice == '4':
            update_movie()
        elif choice == '5':
            # Stats function call here
            pass
        elif choice == '6':
            # Random movie function call here
            pass
        elif choice == '7':
            search_movie()
        elif choice == '8':
            # Movies sorted by rating function call here
            pass
        elif choice == '9':
            create_rating_histogram()
        elif choice == '10':
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter a number between 1 and 10.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
