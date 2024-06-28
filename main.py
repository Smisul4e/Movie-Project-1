from movie_app import MovieApp
from json_storage import StorageJson


def main():
    # Създаване на обект StorageJson с името на файла за съхранение
    storage = StorageJson('movies.json')

    # Създаване на обект MovieApp с обекта StorageJson
    movie_app = MovieApp(storage)

    # Стартиране на приложението
    movie_app.run()


if __name__ == "__main__":
    main()
