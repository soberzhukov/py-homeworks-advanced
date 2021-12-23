import requests
from bs4 import BeautifulSoup
from pprint import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='post')
result_list = list()


def for_for(obj):

    for el in obj:
        if any(x in el for x in KEYWORDS):
            title_el = article.find('a', class_='post__title_link')
            title_result = title_el.text
            time_el = article.find('span', class_='post__time')
            href = title_el['href']
            result = f'<{time_el.text}> - <{title_result}> - <{href}>'
            if result not in result_list:
                result_list.append(result)
            break


for article in articles:
    titles = [x.text.strip().lower() for x in article.find_all('a', class_='post__title_link')]
    hubs = [x.text.strip().lower() for x in article.find_all('a', class_='hub-link')]
    posts_text = [x.text.strip().lower() for x in article.find_all('div', class_='post__text')]

    for_for(posts_text)
    for_for(titles)
    for_for(hubs)


pprint(result_list)
