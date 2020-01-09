import csv
import requests
from bs4 import BeautifulSoup
'''
AJAX  сайт передает запросы  на сервер в HEADERS по опред урлу- в ответ сервер отправляет сырые данные, которые впрыскиваются в текущую страницу
Далее они форматируются под HTML верстку. Это облегчает ситуациЮ- т.к. не нужен суп
можно просто выхватить данные по урлу из HEADERS 
'''
def get_pages(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	pages = soup.find_all('div', class_='wrapper')
	print(pages)
	

def main():

	get_pages('https://www.liveinternet.ru/rating/ru/#geo=ru')





if __name__=='__main__':
	main()