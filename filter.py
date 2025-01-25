from bs4 import BeautifulSoup

# Load your HTML content
with open("filtered_movies.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Find all divs with class "et_pb_text_inner"
et_pb_texts = soup.find_all("div", class_="et_pb_text_inner")

# Open a file to save extracted data
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    for div in et_pb_texts:
        # Find all <a> tags (links) within the div
        links = div.find_all("a")

        for link in links:
            title = link.get_text(strip=True)  # Extract movie title
            url = link["href"]  # Extract movie URL

            output = f"{title} - {url}"  # Format output with title and link
            print(output)  # Print to console
            file.write(output + "\n")  # Save to file

print("\nExtracted content saved to extracted_text.txt")
