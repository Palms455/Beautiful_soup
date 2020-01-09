import csv

def write_csv(data):
	with open('names.csv', 'a') as f:
		writer = csv.writer(f) #delimeter = символ разграничающий данные. 
		# dialect='Excel'
		writer.writerow((data['name'], data['surname'], data['age']))
def write_csv2(data):
	with open('names.csv', 'a') as file:
		order = ['name', 'surname', 'age']
		writer = csv.DictWriter(file, fieldnames=order)

		writer.writerow(data)


def main():
	d = {'name': 'petr', 'surname':'Ivanov', 'age': 21}
	d1 = {'name': 'Ivan', 'surname':'Ivanov', 'age': 18}
	d2 = {'name': 'Ksu', 'surname':'Petrova', 'age': 32}

	l = [d, d1, d2]

	with open('cmc.csv', 'r') as f:
		fieldnames = ['name', 'price', 'ticket', 'url'] # определяем порядок чтения данных
		reader = csv.DictReader(f, fieldnames=fieldnames)
		for row in reader:
			print(row)

if __name__=='__main__':
	main()