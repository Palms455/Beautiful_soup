from peewee import *
from desktop_avito_parsing import Article
from simple_avito_to_sql import get_html, get_site_list
from random import randint
import time


db = PostgresqlDatabase(database='avito', user='postgres', password='1514150', host='localhost')


class BaseModel(Model):
    class Meta:
        database = db

class Seller(BaseModel):

	seller = TextField()

class Product(BaseModel):
	title = TextField()
	price = CharField()
	adress = TextField()
	description = TextField()
	category = CharField()
	seller = ForeignKeyField(Seller, backref = 'product_owner')
	item_id = CharField()



class ProductFoto(BaseModel):
	item_id = TextField()
	image = BlobField()






def main():
	db.connect()
	db.create_tables([Product, ProductFoto, Seller ])
	url = 'https://www.avito.ru/rossiya?q=nintendo+wii&p=1'
	for i in range(1, 5):
		urls = f'https://www.avito.ru/rossiya?q=nintendo+wii&p={str(i)}'
		time.sleep(randint(1,5))
		site_list = get_site_list(get_html(urls))


	for site in  site_list:
		print(site)
		p = Article(site)
		Seller.create(seller = p.data['seller'])
		Product.create(**p.data)
		for foto in p.data['image']:
			ProductFoto.create(image=foto, item_id = p.data['item_id'])






if __name__ == '__main__':
	main()