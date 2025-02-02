import requests
from bs4 import BeautifulSoup
import re

# Loop through letters B to Z
for letter in "bcdefghijklmnopqrstuvwxyz":
    url = f"https://kids-in-mind.com/{letter}.htm"
    print(f"Fetching data from: {url}")

    # Fetch the content of the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the div with the relevant class
        target_div = soup.find("div", class_="et_pb_section et_pb_section_0 et_section_regular")

        if target_div:
            content = target_div.prettify()

            # Regex pattern to capture movie list format
            pattern = re.compile(
                r'(<a href="[^"]+" rel="noopener(?: noreferrer)?" target="_blank">\s*[\s\S]+?</a>\s*\[[0-9]{4}\] \[[A-Z0-9-]+\] – \d+\.\d+\.\d+\s*<br/?>)'
            )

            matches = pattern.findall(content)

            if matches:
                # Print the extracted movies
                for match in matches:
                    print(match + "\n")

                # Save the extracted movies to a file
                with open("filtered_movies.html", "a", encoding="utf-8") as f:
                    for match in matches:
                        f.write(match + "\n\n")

            else:
                print(f"No matching movie lines found for letter {letter}.")
        else:
            print(f"Div not found for letter {letter}.")
    else:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")

print("\nFiltered content saved to filtered_movies.html")