from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


time.sleep(5)  # Wait 5 seconds before extracting elements


# Set up Chrome options for Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

# Specify the path to ChromeDriver
service = Service('C:/chromedriver/chromedriver.exe')

# Start a Selenium WebDriver session
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open IMDb Top 250 page
url = 'https://www.imdb.com/chart/top'
driver.get(url)

# Wait for the page to load and elements to be present
wait = WebDriverWait(driver, 30)  # Wait up to 10 seconds
movies = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td.titleColumn')))
ratings = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td.posterColumn span[name=ir]')))
crew = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'td.titleColumn a')))

# Debug prints to check if the elements are being found
print(f"Found {len(movies)} movies.")
print(f"Found {len(ratings)} ratings.")
print(f"Found {len(crew)} crew members.")

# Create a list to store movie information
movie_list = []

# Iterate through the found elements and extract data
for index in range(len(movies)):
    movie_string = movies[index].text
    movie_title = movie_string.split('\n')[0]
    year = movie_string.split('\n')[1].strip('()')
    place = movie_string.split('.')[0]
    
    # Safely get rating and crew, if available
    rating = ratings[index].get_attribute('data-value') if index < len(ratings) else "N/A"
    star_cast = crew[index].get_attribute('title') if index < len(crew) else "N/A"

    # Store the movie details
    movie_data = {
        "place": place,
        "movie_title": movie_title,
        "rating": rating,
        "year": year,
        "star_cast": star_cast
    }

    movie_list.append(movie_data)

# Print the first few movie entries
for movie in movie_list[:5]:  # Print the first 5 movies
    print(f"{movie['place']} - {movie['movie_title']} ({movie['year']}) - Starring: {movie['star_cast']} - Rating: {movie['rating']}")

page_source = driver.page_source
print(page_source)  # This will print the entire page's HTML content


# Close the driver
driver.quit()
