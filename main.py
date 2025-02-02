import window
import titles  # Import the Python file that contains the movies list

# Extract the movie titles from the list
if hasattr(titles, "movies") and isinstance(titles.movies, list):
    print("Movie Titles:")
    for movie in titles.movies:
        print(movie["title"])  # Access the 'title' field in each dictionary
else:
    print("No movies found or incorrect data format.")


