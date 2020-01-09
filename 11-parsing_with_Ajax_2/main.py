import requests
import csv
from bs4 import BeautifulSoup
import json

'''
сначала парсим первую страницу. Смотрим на кнопку еще и видим что подгружает JS - по опред адресу делается запрос на страницу. 
Если html возвращает в Content-type то парсим как обычно
если возвращается json то в нем возвращается 2 ключа первый - объект Content- type Html 
второй ключ - ссылка на следующую страницу. Далее по циклу проводимся по спискам и парсим данные

'''

def write_csv(data):
	with open('youtube_parse.csv' ,'a') as file:
		order = ['name', 'url']
		writer = csv.DictWriter(file, fieldnames=order)
		writer.writerow(data)

def get_html(url):
	r = requests.get(url)
	return r


def get_page_data(response):
	if 'html' in response.headers['Content-Type']:
		html = response.text
	else:
		html = response.json()['content_html']

	soup = BeautifulSoup(html, 'lxml')
	items = soup.find_all('h3', class_='yt-lockup-title')

	for i in items:
		#name = i.text.strip()
		name =i.find('a').get('title')
		url = 'http://www.youtube.com' + i.find('a').get('href')
		
		data = {'name': name, 'url': url}
		write_csv(data)

def get_next_page(response):
	if 'html' in response.headers['Content-Type']:
		html = response.text
	else:
		html = response.json()['load_more_widget_html']
	soup = BeautifulSoup(html, 'lxml')

	try:
		url = 'https://www.youtube.com'+ soup.find('button', class_='load-more-button').get('data-uix-load-more-href')
	except:
		url = ''
	return url
def main():
	url= 'https://www.youtube.com/user/podval4ikshow/videos'
	
	while True:
		response = get_html(url)
		get_page_data(response)

		url = get_next_page(response)

		if url :
			continue
		else: 
			break

	


if __name__=='__main__':
	main()