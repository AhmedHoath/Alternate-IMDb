import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP GET Request to the page
url = "https://kids-in-mind.com/a.htm"  # Replace with the actual URL
response = requests.get(url)

# Step 2: Check if the page was successfully fetched
if response.status_code != 200:
    print("Failed to retrieve the page.")
    exit()

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Find all the div elements with class 'et_pb_text_inner'
div_elements = soup.find_all('div', class_='et_pb_text_inner')

# Step 5: Print the content inside each div (movie titles or other content)
for div in div_elements:
    print(div.get_text(strip=True))  # This will print the text inside the div without extra whitespace

