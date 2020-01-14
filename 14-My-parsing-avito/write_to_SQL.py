from peewee import *
from desktop_avito_parsing import Article
from simple_avito_to_sql import get_html, get_site_list
from random import randint
import time


db = PostgresqlDatabase(database='avito', user='postgres', password='1514150Ee', host='localhost')


class BaseModel(Model):
    class Meta:
        database = db

class Seller(BaseModel):

	seller = TextField(unique=True)

class Product(BaseModel):
	title = TextField()
	price = CharField()
	adress = TextField()
	description = TextField()
	category = CharField()
	seller = ForeignKeyField(Seller, to_field='seller', related_name = 'product_owner', on_delete='cascade',
                               on_update='cascade')
	item_id = CharField(unique=True)



class ProductFoto(BaseModel):
	item_id = ForeignKeyField(Product, to_field= 'item_id', related_name='phoro_item', on_delete='cascade')
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
		try:
			owner = Seller.get(seller = p.data['seller'])
		except DoesNotExist:
			Seller.create(seller = p.data['seller'])

		Product.create(title=p.data['title'], price=p.data['price'], adress= p.data['adress'], description=p.data['description'], category = p.data['category'], seller=p.data['seller'], item_id=p.data['item_id'])
		for imagin in (p.data['image']):
			#file=open(f'{i}.jpg', 'wb')
			#file.write(imagin)
			#file.close()
			#i +=1
			ProductFoto.create(image = imagin, item_id = p.data['item_id'])




if __name__ == '__main__':
	main()