from lxml import html
import requests
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client['news']


url = 'https://news.mail.ru'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61/63 Safari/537.36'}
response = requests.get(url, headers=headers)
dom = html.fromstring(response.text)

#Отдельно выделил главную новость и остальные новости, т. к. по главной новости есть дополнительный тектстовый  раздел subtitle, который я включил в содержание новости.
#По остальным новостям такого раздела нет
main_news= dom.xpath('//td[@class="daynews__main"]//*/text()')
main_news = [el.replace('\xa0', ' ') for el in main_news]
main_news='. '.join(main_news)
main_news_link = dom.xpath('//td[@class="daynews__main"]//*/@href')
response_d = requests.get(main_news_link[0], headers=headers)
dom_d = html.fromstring(response_d.text)
main_news_date = dom_d.xpath('//span//*//@datetime')


dict1 = {}
dict1['type'] = 'Mail.ru_main_news_with_subtitle'
dict1['content'] =  main_news
dict1['news_link'] = main_news_link[0]
dict1['news_date'] = main_news_date[0]
#Я понял так, что база собирает и НАКАПЛИВАЕТ информацию о новостях за период, поэтому новые новости добавляются к старым, не удаляя их
#(выполняется только проверка на дублирование). Если это не так (нужны только актуальные новости), то в начале кода следует выполнить команду  db.news.drop().
#Но не вижу смысла в базе, имеющей всего 5 записей)
db.news.update_one({'news_link' : dict1['news_link']},{'$set': dict1 }, upsert=True)


other_news= dom.xpath('//td[@class="daynews__items"]/*')
for news in other_news:
    dict2= {}
    dict2['type'] = 'Mail.ru_other_news'
    dict2['content'] = news.xpath('.//text()')[0].replace('\xa0', ' ')
    dict2['news_link'] = news.xpath('.//@href')[0]
    response_l = requests.get(dict2['news_link'], headers=headers)
    dom_l = html.fromstring(response_l.text)
    dict2['news_date'] = dom_l.xpath('//span//*//@datetime')[0]
    db.news.update_one({'news_link' : dict2['news_link']},{'$set': dict2 }, upsert=True)
    
for el in db.news.find({}):
    print (el)
















