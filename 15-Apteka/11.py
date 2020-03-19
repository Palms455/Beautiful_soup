from seleniumwire import webdriver
import requests
import json
# pip install selenium-wire
driver =webdriver.Chrome()
driver.get('https://cenyvaptekah.ru/ufa/amoxicillin_suspenziya_250_mg_5_ml_100_ml_po_receptu')

for request in driver.requests:
	if request.response:
		if request.path == 'https://cenyvaptekah.ru/city/ufa/pharm/basket/index_data':
			cookie = {'cookie': request.headers['cookie']}



url = 'https://cenyvaptekah.ru/city/ufa/pharm/basket/index_data'
response = requests.get(url, params={'mode': 'full'}, cookies=cookie)
print(response.json())




