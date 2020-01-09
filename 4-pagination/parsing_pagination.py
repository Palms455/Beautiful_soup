import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
	r = requests.get(url)
	if r.ok: #True if status 200
		return r.text
	print(r.status_code)

def write_csv(data):
	with open('parsind_data.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([data['name'], data['rating']])
		

def get_page_data(html):
	soup = BeautifulSoup(html,'lxml')
	cards = soup.find_all('div' , class_='WorkersList-WorkerCard') #return list
	for card in cards:
		try:
			name = card.find('a', class_='WorkerCard-Title').text
			rate = card.find('b', class_='Text').text
		except:
			name = ''
		data = {'name' : name, 'rating': rate }
		write_csv(data)

def main():
	url = 'https://yandex.ru/uslugi/11116-sterlitamak/category/perevozki-i-kureryi--178?p={}'
	for i in range(0, 86):
		url = url.format(str(i))
		get_page_data(get_html(url))

if __name__=='__main__':
	main()