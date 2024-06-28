from json_storage import JSONStorage

# Създаване на инстанция на JSONStorage
storage = JSONStorage('test_movies.json')

# Тест на list_movies()
print("Initial movies list:")
print(storage.list_movies())

# Тест на add_movie()
print("\nAdding a new movie 'Inception'...")
storage.add_movie('Inception', 2010, 8.8, 'https://link-to-poster.com/inception.jpg')
print("Movies list after adding 'Inception':")
print(storage.list_movies())

# Тест на add_movie() за още един филм
print("\nAdding another movie 'The Matrix'...")
storage.add_movie('The Matrix', 1999, 8.7, 'https://link-to-poster.com/matrix.jpg')
print("Movies list after adding 'The Matrix':")
print(storage.list_movies())

# Тест на update_movie()
print("\nUpdating rating of 'Inception' to 9.0...")
storage.update_movie('Inception', 9.0)
print("Movies list after updating 'Inception':")
print(storage.list_movies())

# Тест на delete_movie()
print("\nDeleting 'The Matrix'...")
storage.delete_movie('The Matrix')
print("Movies list after deleting 'The Matrix':")
print(storage.list_movies())
