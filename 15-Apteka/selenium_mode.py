from selenium import webdriver
import time
from bs4 import BeautifulSoup
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
			button.click()
			time.sleep(1)
		
	def navigate(self):
		self.driver.get(self.url)
		self.driver.find_element_by_css_selector('.alert-first-usage__content a').click()
		print(self.driver.get_cookies())
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
		self.in_basket()
		

	def in_basket(self):
		self.driver.get('https://cenyvaptekah.ru/city/ufa/pharm/basket/index')
		self.driver.implicitly_wait(3)
		adress = self.driver.find_elements_by_css_selector('div#basketGoodTable>div>div.row-fluid')
		items = self.driver.find_elements_by_css_selector("div#basketGoodTable>div>div[sssid='basketGoodTable']")
		for adres, item in zip(adress, items):
			item_adres = adres.find_element_by_css_selector('div.span12>a').text
			items_list = item.find_element_by_css_selector('tbody#basketRowsBody').find_elements_by_tag_name('tr')
			for pharm in items_list:
				pharm_name = pharm.find_element_by_tag_name('a').text
				pharm_quantity = pharm.find_element_by_css_selector('td.basket-col-rest span.price_grid').text
				price = pharm.find_element_by_css_selector('td.price div span').text
				data = {'pharm_name': pharm_name,
						'pharm_adres': item_adres,
						'price': price,
						'pharm_quantity': pharm_quantity}
				self.write_csv(data)
		self.driver.close()


	def write_csv(self, data):
		with open('new_cmc.csv', 'a',encoding='utf-8') as file:
			order = ['pharm_name', 'pharm_adres', 'price', 'pharm_quantity']
			writer = csv.DictWriter(file, fieldnames=order)
			writer.writerow(data)





if __name__ == '__main__':
	b = Bot('https://cenyvaptekah.ru/ufa/amoxicillin_suspenziya_250_mg_5_ml_100_ml_po_receptu')

