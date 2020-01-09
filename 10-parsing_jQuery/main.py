import requests
import csv
from bs4 import BeautifulSoup

'''
парсинг jQuery необходим например когда организована не постраничная верстка сайтов
а через впрыскивание данных в html - лента данных.

Если при парсинге через реквест сайт выдает статус 400- значит необходимы данные заголовков. Обычно они подбираются опытым путем
'''

def get_html(url):
	user_agent = { 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}
	r = requests.get(url, headers = user_agent)
	print(r.status_code)
	return r.text


def write_csv(data):
	with open('catertrax.csv', 'a') as file:
		order = ['author', 'since']
		writer = csv.DictWriter(file, fieldnames = order)
		writer.writerow(data)

# 1 получение контейнера с отзывами и списка отзывов
# 2 если список есть парсим отзывы
# 3 если список пустой -цикл прерывается
def get_articles(html):
	soup = BeautifulSoup(html, 'lxml')
	container =soup.find('div', class_='testimonial-container').find_all('article')
	return container # вернет либо пустой список, либо спиок тэгов с отзывами

def page_data(container):
	for cont in container:
		try:
			since = cont.find('p', class_='traxer-since').text.strip()
		except:
			since = ''
		try:
			author = cont.find('p', class_='testimonial-author').text.strip()
		except:
			author = ''
		data = {'author': author, 'since': since}
		write_csv(data)




def main():
	page = 1
	while True:
		url = 'https://catertrax.com/why-catertrax/traxers/page/{}'.format(str(page))

		articles = get_articles(get_html(url))

		if articles:
			page_data(articles)
			page +=1
		else:
			break



if __name__=='__main__':
	main()