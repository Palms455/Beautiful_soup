import csv
import requests
from bs4 import BeautifulSoup
'''
AJAX  сайт передает запросы  на сервер в HEADERS по опред урлу- в ответ сервер отправляет сырые данные, которые впрыскиваются в текущую страницу
Далее они форматируются под HTML верстку. Это облегчает ситуациЮ- т.к. не нужен суп
можно просто выхватить данные по урлу из HEADERS 
'''

def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('websites.csv', 'a', encoding='utf-8') as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def main():

    for i in range(0, 6428):
        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(i))
        response = get_html(url)
        data = response.strip().split('\n')[1:]

        for row in data:
            columns = row.strip().split('\t')
            name = columns[0]
            url = columns[1]
            description = columns[2]
            traffic = columns[3]
            percent = columns[4]

            data = {'name': name,
                    'url': url,
                    'description': description,
                    'traffic': traffic,
                    'percent': percent}
            write_csv(data)






if __name__ == '__main__':
    main()
