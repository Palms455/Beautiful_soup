import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def get_html(url, num_retries=2):
	'''
	num retries нужен для повторной попытки скачивания ресурса
	'''
	print('Загрузка:', url)
	try:
		html = urllib.request.urlopen(url).read()
	except (URLError, HTTPError, ContentTooShortError) as e:
		print('Ошибка загрузки:', e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code <= 600:
				return get_html(url, num_retries - 1)
		#при ошибкии 500 повторная попытка скачивания
	return html




if __name__ == '__main__':
	url = 'https://www.httpbin.org/status/500'
	print(get_html(url))