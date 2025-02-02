import window
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("titles.db")
cursor = conn.cursor()

# Query to get all movie titles from the database
cursor.execute("SELECT title FROM movies")

# Fetch all results
movies = cursor.fetchall()

# Print all movie titles
if movies:
    print("Movie Titles in the Database:")
    for movie in movies:
        print(movie[0])  # Each 'movie' is a tuple, so we print the title which is at index 0
else:
    print("No movies found in the database.")

# Close the database connection
conn.close()

