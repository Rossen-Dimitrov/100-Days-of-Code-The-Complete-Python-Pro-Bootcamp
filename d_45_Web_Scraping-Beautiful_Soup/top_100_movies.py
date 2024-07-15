from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_page = response.text

soup = BeautifulSoup(movie_page,'html.parser')
all_movies = soup.find_all(name='h3', class_='listicleItem_listicle-item__title__BfenH')
all_movies.reverse()
for movie in all_movies:
    print(movie.getText())