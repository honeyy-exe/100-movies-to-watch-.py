# 🎬 100 Movies to Watch Scraper
# This script scrapes the "Top 100 Movies to Watch" list from Empire Online (archived version)
# and saves them in order to a text file.

from bs4 import BeautifulSoup   # BeautifulSoup helps us parse (read) HTML easily
import requests                 # Requests helps us download the web page

# ✅ 1. The URL we want to scrape (using Wayback Machine archived version)
URL = (
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)

# ✅ 2. Fetch the webpage using requests
response = requests.get(URL)          # Makes an HTTP GET request to the URL
website_html = response.text          # Gets the HTML content as text

# ✅ 3. Parse the HTML with BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# ✅ 4. Find all the movie titles (they are in <h3 class="title"> tags)
all_movies = soup.find_all(name="h3", class_="title")

# ✅ 5. Extract just the text (movie names) from the tags
movie_titles = [movie.getText() for movie in all_movies]

# ✅ 6. The website lists movies from 100 → 1,
# but we want them from 1 → 100, so we reverse the list
movies = movie_titles[::-1]

# ✅ 7. Save the movie list to a text file
# We use UTF-8 encoding so special characters (like é, ü, etc.) don’t cause errors
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(movie + "\n")  # Write each movie on a new line

print("✅ Done! Check movies.txt for the full list 🎉")
