import csv
from peewee import *

'''
Для работы с СУБД можно использовать ORM peewee
pip install peewee psycopg2 psycopg2-binary
sudo apt-get install postgresql pgadmin3

sudo -u postgres psql :enter to bd
\password :new pass
CREATE DATABASE test; : new database



'''
db = PostgresqlDatabase(database='test', user='postgres', password='1514150Ee', host='localhost')
class Coinses(Model):
	name = CharField(max_length=60)
	url = TextField()
	price = CharField()
	ticket = CharField()

	class Meta:
		database = db



def main():
	db.connect() #поключ к бд
	db.create_tables([Coinses]) #создание таблицы название класса выше


	with open('cmc.csv', 'r') as file:
		order = ['name', 'price', 'ticket', 'url'] # именовать переменные нужно в том порядке, в каком их скачивали в CSV
		 
		reader = csv.DictReader(file, fieldnames=order)
		
		coins = list(reader)
		
		# №1 плохой способ
		#for row in coins:
		#	coin = Coin(name=row['name'], price=row['price'], ticket=row['ticket'], url=row['url'])
		#	coin.save()

		# №2 через транзакции peeweeManager
		with db.atomic():
			for row in coins:
		 		Coinses.create(**row) ## **- неогранич список позиц аргументов
		# №3 через индексы и слайсы
		with db.atomic():
			for index in range(0, len(coins), 100):
				Coinses.insert_many(coins[index:index+100]).execute()




if __name__=='__main__':
	main()