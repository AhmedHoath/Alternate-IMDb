from bs4 import BeautifulSoup
import re

# Load your HTML content
with open("filtered_movies.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Find all divs with class "et_pb_text_inner"
et_pb_texts = soup.find_all("div", class_="et_pb_text_inner")

# Extract and print the text content
for div in et_pb_texts:
    print(div.get_text(separator="\n", strip=True))

# Save the extracted text to a file
with open("extracted_titles.txt", "w", encoding="utf-8") as file:
    for div in et_pb_texts:
        file.write(div.get_text(separator="\n", strip=True) + "\n")




# Load your HTML content
with open("filtered_movies.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Find all divs with class "et_pb_text_inner"
et_pb_texts = soup.find_all("div", class_="et_pb_text_inner")

# Open a file to save extracted data
with open("extracted_links.txt", "w", encoding="utf-8") as file:
    for div in et_pb_texts:
        # Find all <a> tags (links) within the div
        links = div.find_all("a")

        for link in links:
            title = link.get_text(strip=True)  # Extract movie title
            url = link["href"]  # Extract movie URL

            # Format output with title and link and print to console
            output = f"{title} - {url}"
            print(output)
            file.write(output + "\n")  # Save to file

        # Extract and print the text content from the div
        div_text = div.get_text(separator="\n", strip=True)
        print(div_text)
        file.write(div_text + "\n")  # Save the text content to file

print("\nExtracted content saved to extracted_links.txt")






def remove_time_from_files():
    # Read and clean extracted_titles.txt
    with open("extracted_titles.txt", "r", encoding="utf-8") as file:
        titles = file.readlines()

    with open("extracted_titles.txt", "w", encoding="utf-8") as file:
        for title in titles:
            cleaned_title = title.replace("TIME", "")  # Remove the word "TIME"
            file.write(cleaned_title)

    # Read and clean extracted_links.txt
    with open("extracted_links.txt", "r", encoding="utf-8") as file:
        links = file.readlines()

    with open("extracted_links.txt", "w", encoding="utf-8") as file:
        for link in links:
            cleaned_link = link.replace("TIME", "")  # Remove the word "TIME"
            file.write(cleaned_link)

    print("The word 'TIME' has been removed from both files.")

# Call the function to clean the files
remove_time_from_files()







def add_line_separator_to_organizers():
    # Read extracted_titles.txt and extracted_links.txt
    with open("extracted_titles.txt", "r", encoding="utf-8") as file:
        titles = file.readlines()

    with open("extracted_links.txt", "r", encoding="utf-8") as file:
        links = file.readlines()

    # Add "---------------" before letter organizers in titles
    with open("extracted_titles.txt", "w", encoding="utf-8") as file:
        for title in titles:
            # Match "Movie Reviews by Title | LETTER" and add "---------------" before if found
            if re.match(r"Movie Reviews by Title \| [A-Za-z]", title):
                title = "-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-" + title.strip()+"\n"  # Prepend "---------------" before the title
            file.write(title)

    # Add "---------------" before letter organizers in links
    with open("extracted_links.txt", "w", encoding="utf-8") as file:
        for link in links:
            # Match "Movie Reviews by Title | LETTER" and add "---------------" before if found
            if re.match(r"Movie Reviews by Title \| [A-Za-z]", link + "\n"):
                link = "-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-" + link.strip()+"\n"  # Prepend "---------------" before the link
            file.write(link)

    print("Added '-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-$-' before letter organizers in both files.")

# Call the function to add separators to letter organizers
add_line_separator_to_organizers()