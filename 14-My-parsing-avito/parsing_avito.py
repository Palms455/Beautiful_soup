import requests
import csv
from bs4 import BeautifulSoup



def get_html(url):
	r = requests.get(url)
	if r.ok:
		return r.text
	else:
		print(r.status_code)

def get 

def get_list_urls(html): 
	# found count pages
	soup = BeautifulSoup(html, 'lxml')
	page_count = soup.find('span', {"data-marker" : "pagination-button/next"}).find_previous_sibling('span').text
	return page_count

def main():
	url = 'https://www.avito.ru/rossiya?q=nintendo+wii&p=1'
	for i in range(1,get_list_urls(get_html(url))):
		urls = f'https://www.avito.ru/rossiya?q=nintendo+wii&p={str(i)}'


if __name__ == '__main__':
	main()