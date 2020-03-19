from seleniumwire import webdriver
import time
from bs4 import BeautifulSoup
import requests
import csv

class Bot:
	def __init__(self, url):
		self.url = url
		#self.options = webdriver.ChromeOptions()
		#self.options.add_argument('headless')  # для открытия headless-браузера
		#self.driver= webdriver.Chrome(options=self.options)
		self.driver = webdriver.Chrome()
		self.navigate()

	def add_basket(self):
		buttons = self.driver.find_elements_by_css_selector('.row-fluid>.buy-btn-div>a.btn.btn-info')
		for button in buttons:
			try:
				button.click()
				time.sleep(1.5)
			except:
				alert_obj = self.driver.switch_to.alert
				alert_obj.accept()
				time.sleep(5)
				button.click()
		
	def navigate(self):
		self.driver.get(self.url)
		self.driver.find_element_by_css_selector('.alert-first-usage__content a').click()
		for request in self.driver.requests:
			if request.response:
				if request.path == 'https://cenyvaptekah.ru/city/ufa/pharm/basket/index_data':
					cookie = {'cookie': request.headers['cookie']}
					print('get cookies')
		next_page = self.driver.find_element_by_css_selector('div.dataTables_paginate.paging_bootstrap.pagination ul :nth-child(5)')
		while True:
			self.driver.implicitly_wait(0.2)
			self.driver.execute_script("window.scrollTo(0, 0);")
			time.sleep(0.1)
			self.add_basket()
			if 'disabled' not in next_page.get_attribute('class'):
				next_page.find_element_by_tag_name('a').click()
			else:
				break

		self.driver.close()
		print('close selenium')
		self.get_basket(cookie)
		print('Loaded done!')

		

	def get_basket(self, cookie):
		url = 'https://cenyvaptekah.ru/city/ufa/pharm/basket/index_data'
		print(cookie)
		response = requests.get(url, params={'mode': 'full'}, cookies=cookie)
		data = response.json()['pharms']
		print('get response')
		print(data)
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
				self.write_csv(pharm)

		
	def write_csv(self, pharm):
		with open('grm.csv', 'a',encoding='utf-8') as file:
			order = ['pharm_name', 'pharm_adres', 'price', 'quantity']
			writer = csv.DictWriter(file, fieldnames=order)
			print('write in to csv')
			writer.writerow(data)




if __name__ == '__main__':
	b = Bot('https://cenyvaptekah.ru/ufa/amoxicillin_hemofarm_kapsuly_500_mg_16_sht_')

