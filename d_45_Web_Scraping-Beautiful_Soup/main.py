from bs4 import BeautifulSoup
import requests


class Article:
    def __init__(self, text, link, a_id, score=0):
        self.a_id = a_id
        self.text = text
        self.link = link
        self.score = score

    def __repr__(self):
        return f"Article(a_id={self.a_id}, score={self.score}, text={self.text}, link={self.link})"


articles = []

URL = 'https://news.ycombinator.com/'
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
athing_elements = soup.find_all('tr', class_='athing')
scores = soup.find_all(class_='score')

for athing in athing_elements:
    athing_id = athing.get('id')
    titleline_span = athing.find('span', class_='titleline')
    if titleline_span:
        first_a = titleline_span.find('a')
        if first_a:
            a_text = first_a.get_text()
            a_link = first_a.get('href')
            points = athing.find('div', id='points')
            articles.append(Article(text=a_text, a_id=athing_id, link=a_link))

for article in articles:
    article_id = 'score_' + article.a_id
    element = soup.find(id=article_id).getText()
    article.score = int(element.split()[0])

highest_score_article = max(articles, key=lambda article: article.score)

print("Article with the highest score:", highest_score_article)
