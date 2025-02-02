import re

# Function to parse the titles file and filter data
def parse_and_save_titles(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    current_index = None  # This will store the current letter index (A, B, etc.)
    line_iter = iter(lines)  # Convert lines into an iterator

    movies = []  # List to store movie data as dictionaries

    for line in line_iter:
        line = line.strip()

        if line.startswith("-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-Movie Reviews by Title |"):
            # Extract the letter index from the line
            match = re.search(r"Movie Reviews by Title \| (\w)", line)
            if match:
                current_index = match.group(1)
        
        # Process movie title and details (ignoring empty lines)
        elif line and not line.startswith("-"):
            # Match the movie title pattern
            title_match = re.match(r"^(.*)$", line)
            
            # Get the next line for details
            next_line = next(line_iter, "").strip()  
            
            # Improved regex pattern to allow for flexibility with spaces and separators
            details_match = re.match(r"\[(\d{4})\] \[([A-Za-z0-9\-]+)\] – (\d+\.\d+\.\d+)", next_line)

            if title_match and details_match:
                title = title_match.group(1).strip()
                year = int(details_match.group(1))
                age = details_match.group(2)
                
                # Split the sex, violence, and language levels
                sex_nudity, violence_gore, language = map(int, details_match.group(3).split("."))

                # Debugging: print title and details to verify correct data extraction
                print(f"Processing: {title} ({year})")

                # Store the movie data as a dictionary
                movie_data = {
                    "title": title,
                    "letter_index": current_index,
                    "year": year,
                    "age": age,
                    "sexNudity": sex_nudity,
                    "violenceGore": violence_gore,
                    "language": language
                }

                # Add to the list of movies
                movies.append(movie_data)
            else:
                # Print skipped titles and their details
                print(f"Skipping: {line}, Details: {next_line}")

    # Write the movie data to a Python file (titles.py)
    with open("titles.py", "w", encoding="utf-8") as py_file:
        py_file.write("movies = [\n")
        for movie in movies:
            py_file.write(f"    {movie},\n")
        py_file.write("]\n")

    print(f"Processed and saved {len(movies)} movies to titles.py")

# Run the function to parse the file and save data
parse_and_save_titles("extracted_titles.txt")
