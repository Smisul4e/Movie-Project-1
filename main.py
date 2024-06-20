from movies import (
    list_movies,
    add_movie,
    delete_movie,
    update_movie,
    stats,
    random_movie,
    search_movie,
    movies_sorted_by_rating
)

def main():
    while True:
        print("********** My Movies Database **********")
        print("\nMenu:")
        print("1. List movies")
        print("2. Add movie")
        print("3. Delete movie")
        print("4. Update movie")
        print("5. Stats")
        print("6. Random movie")
        print("7. Search movie")
        print("8. Movies sorted by rating")
        print("9. Exit")

        choice = input("\nEnter choice (1-9): ")
        if choice == '1':
            list_movies()
        elif choice == '2':
            add_movie()
        elif choice == '3':
            delete_movie()
        elif choice == '4':
            update_movie()
        elif choice == '5':
            stats()
        elif choice == '6':
            random_movie()
        elif choice == '7':
            search_movie()
        elif choice == '8':
            movies_sorted_by_rating()
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
        print()

if __name__ == "__main__":
    main()
