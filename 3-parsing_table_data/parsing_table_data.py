import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
	r = requests.get(url)
	return r.text

def write_csv(data):
	with open('coin.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([data['name'],data['ticket'], data['price'], data['url']])

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('tbody').find_all('tr', class_='cmc-table-row')
	for tr in table:
		tds = tr.find_all('td')
		name = tds[1].find('a').text
		ticket = ((tds[5].text).split())[1]
		url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
		price = tds[3].find('a').text.split('$')[1].replace(',','')
		data = {'name': name, 'ticket': ticket, 'url': url, 'price':price}
		write_csv(data)


def main():
	url = 'https://coinmarketcap.com/'
	get_page_data(get_html(url))


if __name__=='__main__':
	main()