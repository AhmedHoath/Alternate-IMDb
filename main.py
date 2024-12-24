from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import json
from flask import Flask, jsonify
from flask_cors import CORS

# Flask app setup
app = Flask(__name__)
CORS(app)

# Scrape IMDb data
def scrape_imdb():
    url = "https://www.imdb.com/chart/top/"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve the page, status code: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []
    for item in soup.select('td.titleColumn'):
        title = item.a.text
        year = item.span.text.strip("()")
        movies.append({"title": title, "year": year})

    # Save scraped data to a JSON file
    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)

    return movies



# Endpoint to serve scraped data
@app.route('/movies', methods=['GET'])
def get_movies():
    with open("movies.json", "r") as file:
        movies = json.load(file)
    return jsonify(movies)


print("Scraping IMDb data...")
scrape_imdb()  # Perform scraping when the server starts
print("Starting Flask server...")
app.run(debug=True)
