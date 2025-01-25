from bs4 import BeautifulSoup

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

from bs4 import BeautifulSoup

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

