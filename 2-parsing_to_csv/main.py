import requests

from bs4 import BeautifulSoup
import csv

def write_csv(data):
	with open('plugins.csv', 'a') as f:
	#w write data
	#a append data
		writer = csv.writer(f)
		writer.writerow((data['name'],
						 data['url'],
						 data['reviews'])) #writerow given one arg. we need create tuple or  listg


def get_html(url):
	r = requests.get(url)
	return r.text

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	popular = soup.find_all('section')[1]
	plugins = popular.find_all('article')
#fin_all находит все элеиенты с тегом/ [1]  выбираем второй элемент
# возвращает список object soup
	for plugin in plugins:
		name = plugin.find('h2').text #parsing name
		url = plugin.find('h2').find('a').get('href') #parsing link urk
		r = plugin.find('span', class_='rating-count').find('a').text
		rating = refind(r)

		data={'name': name, 'url': url, 'reviews': rating }
		write_csv(data)
		

def refind(s): #cwe clean string 
	#1,470 total ratings
	r = s.split()[0]
	r = r.replace(',','')
	return r


def main():
	url = 'https://wordpress.org/plugins'
	get_data(get_html(url))


if __name__ == '__main__':
	main()