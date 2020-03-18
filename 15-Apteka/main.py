import requests
import csv
from bs4 import BeautifulSoup
import sys
from selenium_mode import Bot
from multiprocessing import Pool

def get_html(url):
	user_agent = { 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}
	r = requests.get(url, headers = user_agent)
	print(r.status_code)
	return r.text

def get_data(html):
	links = set()
	soup = BeautifulSoup(html, 'lxml')
	link_goods = soup.find_all('a', class_='nodecor')
	for i in link_goods:
		#print(i)
		if '0.00 руб.' not in i.find('span', class_='price_grid').text:
			links.add(('https://cenyvaptekah.ru' + i.get('href')))
	print(links)
	return links

def groups(html):
	biz = set()
	soup = BeautifulSoup(html, 'lxml')
	gr = soup.find_all('div', {'class': 'span4 mb-10'})
	for i in gr:
		links = 'https://cenyvaptekah.ru' + i.find('a').get('href')
		urls = get_data(get_html(links))
		if urls:
			for i in urls:
				data = Bot(i)



if __name__ == '__main__':
	url = 'https://cenyvaptekah.ru/ufa/antibiotiki'
	groups(get_html(url))
	#links = get_data(get_html(url))
	#print(links)
	#with Pool(2) as pool:
	#	#Pool.map() принимает имя функции и итерируемое множество (список, например) аргументов, для которой она будет выполняться
	#	pool.map(Bot, links)