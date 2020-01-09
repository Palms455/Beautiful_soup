import requests
from bs4 import BeautifulSoup
from random import choice
"""
распарсим сайт со списком прокси
"""

def get_html(url):
	#proxies = {'https': 'ipaddress: 5000'}
	p = get_proxy() #{'schema': '' , 'adress': ''}
	proxy = {p['schema']: p['adress']} # можно указать несколько прокси
	
	r = requests.get(url, proxies=proxy, timeout=5 )
	return r.json()['origin']

def get_proxy():
	html = requests.get('https://free-proxy-list.net/').text
	proxies = []
	soup = BeautifulSoup(html, 'lxml')
	trs = soup.find('table', id= 'proxylisttable').find('tbody').find_all('tr')[:12]
	for tr in trs:
		tds = tr.find_all('td')
		adress = tds[0].text.strip()
		port = tds[1].text.strip()
		schema = 'https' if 'yes' in tds[6].text.strip() else 'http'
		proxy = {'schema': schema, 'adress': adress + ':' + port}

		proxies.append(proxy)
	return choice(proxies) #функция берет на вход список эелемнтов и возвращает рандомное значение из него






def main():
	url = 'http://httpbin.org/ip'
	get_proxy()
	print(get_html(url))


if __name__=='__main__':
	main()