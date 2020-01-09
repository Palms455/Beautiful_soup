
from selenium import webdriver




class Bot:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.navigate()

	def navigate(self):
		self.driver.get('https://www.avito.ru/sterlitamak/kvartiry/5-k_kvartira_95_m_35_et._1880771623')
		button = self.driver.find_element_by_class('BPWk2').click()
		




def main():
	link = 'https://www.avito.ru'
	b = Bot()




if __name__=='__main__':
	main()