import requests
from bs4 import BeautifulSoup

url = 'https://wordpress.org/'

def get_html(url):
	r = requests.get(url)
	return r.text

def get_data(html):
	soup = BeautifulSoup(html, 'lxml') #lxml recomended parser
	h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
	return h1

def main():
	url = 'https://wordpress.org/'
	print(get_data(get_html(url)))



if __name__ == '__main__':
	main()
