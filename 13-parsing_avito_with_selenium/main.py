
from selenium import webdriver
import time
from PIL import Image
from pytesseract import image_to_string
'''
pip3 install pillow
from PIL import Image работа с изображением
'''

class Bot:
	def __init__(self):
		self.options = webdriver.ChromeOptions()
		self.options.add_argument('headless')  # для открытия headless-браузера
		self.driver= webdriver.Chrome(chrome_options=self.options)
		#self.driver = webdriver.Chrome()
		self.navigate()
		self.driver.implicitly_wait(5)

	def take_screenshot(self):
		self.driver.save_screenshot('avito_screenshot.png')

	def navigate(self):
		self.driver.get('https://www.avito.ru/sterlitamak/kvartiry/5-k_kvartira_95_m_35_et._1880771623')
		button = self.driver.find_element_by_class_name('item-phone-button_hide-phone').click()
		time.sleep(3)
		self.take_screenshot()
		image = self.driver.find_element_by_css_selector('.item-phone-big-number img')
		location = image.location
		size = image.size
		print(location, size)

		self.crop(location, size)

	def tel_recon(self):
		image = Image.open('tel.gif')
		print(image_to_string(image))

	def crop(self, location, size): # работаем с изображением.
		image = Image.open('avito_screenshot.png')
		x = location['x'] #задаем параметры и его размеры
		y = location['y']
		width = size['width']
		height = size['height']
		image.crop((x,y, x+width, y+height)).save('tel.gif')
		self.tel_recon()



"""
для распознавания изображения необходимо установить тессеракт
 sudo apt-get install tesseract-ocr
 pip install pillow
 pip install pytesseract

"""



def main():
	link = 'https://www.avito.ru'
	b = Bot()
	




if __name__=='__main__':
	main()