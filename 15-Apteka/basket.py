import requests
import json
import csv
from bs4 import BeautifulSoup


def get_basket(cookie):
	url = 'https://cenyvaptekah.ru/city/ufa/pharm/basket/index_data'
	response = requests.get(url, params={'mode': 'full'}, cookies=cookie)
	data = response.json()['pharms']
	for pharm_data in data:
		apteka = pharm_data['pharm_data']['name'] + pharm_data['pharm_data']['address']
		for drug in pharm_data['goods']:
			pharm_name = drug['good_name']
			price = drug['price']
			quantity = drug['rest']
			pharm = {'pharm_name': pharm_name,
					'pharm_adres': apteka,
					'price': price,
					'quantity': quantity,
					}
			write_csv(pharm)
		
def write_csv(data):
		with open('Pharm.csv', 'a',encoding='utf-8') as file:
			order = ['pharm_name', 'pharm_adres', 'price', 'quantity']
			writer = csv.DictWriter(file, fieldnames=order)
			writer.writerow(data)


def offers(url, cookie):
	add_params = {}
	goods = []
	response = requests.get(url)
	print(response.status_code)
	data = BeautifulSoup(response.text, 'lxml')
	basket = data.select('.row-fluid>.buy-btn-div>a.btn.btn-info')
	for item in basket:
		dat = item.get('onclick')[28:-1].split(',')
		add_params['good_id'] = dat[0]
		add_params['pharm_id'] = dat[1]
		add_params['offer_id'] = dat[2]
		#add_params['price'] = dat[3]
		add_params['is_ad'] = dat[4]
		goods.append(add_params)
		add_basket(add_params, cookie)
		print('drug added in basket!')
	get_basket(cookie)
	delete_basket(cookie, goods)


def add_basket(add_params, cookie):
	url = 'https://cenyvaptekah.ru/basket/add'
	response = requests.post(url, params=add_params, cookies=cookie)
	print(response)

def delete_basket(cookie, goods):
	url = 'https://cenyvaptekah.ru/basket/del'
	for item in goods:
		response = requests.post(url, params=item, cookies=cookie)
		print(f'Delete status{response.status_code}')













if __name__ == '__main__':
	cookie = {'cookie': '__cfduid=d50e2b855ae9845ca3484e55d9dbd93271584556387; tval=top_buy; _PricesInPharm_session=BAh7DEkiD3Nlc3Npb25faWQGOgZFVEkiJWMwZTU0MDUzNTUxZjllMGYyMzkyMzc0ZTFjYmY4NDE5BjsAVEkiB3N0BjsARkkiDzE1ODQ1NTYzODcGOwBGSSIHY3QGOwBGSSIPMTU4NDU1NjM4NwY7AEZJIgZxBjsARkkiBjAGOwBGSSIHcWEGOwBGSSIGMAY7AEZJIgZhBjsARkkiB1tdBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXRaRVNoNi9jaWI4Y2dZN1BLMExzdzhXNEc3YUYxbTV1TlpZV2tQelVrMUk9BjsARg%3D%3D--eb1977b17152816b657208df57b78bb90fe5fa35; city_ufa_areas=; pharm_type=pharm; city=ufa; text=; _ga=GA1.2.993644358.1584556388; _gid=GA1.2.612080794.1584556388; _ym_uid=1584556388987783234; _ym_d=1584556388; test=1; __utma=265944989.993644358.1584556388.1584556388.1584556388.1; __utmc=265944989; __utmz=265944989.1584556388.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _ym_visorc_24215119=w; top100_id=t1.4469532.296949769.1584556389246; _ym_isad=2; tmr_lvid=063ef87fbb5ef3b6540ef57c5d06901d; tmr_lvidTS=1584556389278; f=1; isbliz=0; basket=3bc652a0-5dbe-49be-a4fa-e13a4a7511ad; basket_hash=b13acca9d72b757f9cd0a4c04096e363200277e5d3099b5b324e88e711f12fa7; _gat_gtag_UA_48328690_1=1; __utmb=265944989.6.10.1584556388; last_visit=1584538554580::1584556554580; tmr_detect=0%7C1584556558570; tmr_reqNum=19'}
	#get_basket(cookie)
	url = 'https://cenyvaptekah.ru/ufa/augmentin_poroshok_dlya_prigotovleniya_suspenzii_dlya_priema_vnutr_125_mg__31_25_mg_5_ml'
	offers(url, cookie)
#seleniumrequests