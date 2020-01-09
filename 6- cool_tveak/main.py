from bs4 import BeautifulSoup
import re





'''
find()  возвращает первый попавшийся элемент
fond_all() возвращает список из найденных объектов
в значениях атрибутов можно указывать как class_= row или как словарь {'class': 'row'}
это полезно когда класс указывается не в одно слово как data-set btn-prymary

если надо найти не сверху вниз а снизу вверх
свойство parent
alena = soup.find('div', text = 'Alena').parent найдет все содержимое БЛИЖАЙШЕГО родительского контейнера
т.е. все во что вложен такой тэг
find_parent(class_='row')- найдет первого родителя искомого тэга с заданным параметром

Движение в стороны. Если необходим поиск по одноранговой иерархии 
find_next_sibling() следующий тэг вправо
find_previous_sibling() предыдущий тэг влево

Фильтрующие функции:

'''
def get_salary(s):
	#salary: 2700 usd per month
	pattern = r'\d{1,9}'
	#salary = re.findall(pattern, s) возвращает всегда список
	salary = re.search(pattern, s)group()

def get_copywriter(tag):
	whois = tag.find('div', id='whois').text.strip()
	if 'Copywriter' in whois:
		return tag
	return None

def main():
	file = open('index.html').read()
	soup = BeautifulSoup(file, 'lxml')
	row = soup.find('div', {'class': 'row'}).text
	copywriters = []
	persons = soup.find_all('div', class_='row')
	for person in persons:
		cw = get_copywriter(person)
		if cw:
			copywriters.append(cw)
	#print(copywriters)

#регулярные выражения

	salary = soup.find_all('div', {'data-set': 'salary'})
	# или salary = soup.find_all('div', text=re.compile('\d{1,9}'))
	# ^ begin str
	# $ ending string
	
	for i in salary:
		#get_salary(i.text)


	



if __name__=='__main__':
	main()