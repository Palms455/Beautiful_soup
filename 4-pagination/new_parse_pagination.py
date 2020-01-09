import requests
from bs4 import BeautifulSoup
import csv
import re


def get_html(url):
		r = requests.get(url)
		if r.ok:
			return r.text
		print(r.status_code)

def write_csv(data):
	with open('cmc.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(data)



def get_page(html):
	soup = BeautifulSoup(html, 'lxml')
	trs = soup.find('tbody').find_all('tr')
	for tr in trs:
		tds = tr.find_all('td') #return list of tags
		
		try:
			name = tds[1].find('a').text
			price = tds[3].find('a').text.replace(',','')
			ticket = tds[5].find('div').text.split()[1]
			url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
			
		except:
			name=''
			price=''
			ticket=''
		data = [name, price, ticket, url]
		write_csv(data)



def main():
	url = 'https://coinmarketcap.com/'

	while True:
		get_page(get_html(url))
		

		soup = BeautifulSoup(get_html(url), 'lxml')
		try:
			pattern ='Next'
			url = 'https://coinmarketcap.com'+ soup.find('div', class_='cmc-button-group').find('a', text=re.compile(pattern)).get('href')
			print(url)

		except:
			break

if __name__=='__main__':
	main()
