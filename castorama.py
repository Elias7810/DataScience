#Фото со страницы получилось скачать только одно, правда, большое) Все остальные
# ссылки на странице товара,ведущие на фотографии, в браузере выглядят нормально, а в scrapy ссылка превращается
# в нечто вида "data:image/png base64 , набор символов". Это каcается всех ссылок на фото с тегом
#src. Единственная работающая ссылка такого тега не имеет. Какие пути в scrapy не подставляй,
#если в конце этого пути будет src - ссылка не обрабатывается((. Возможно, сайт блокирует?

import scrapy
from scrapy.http import HtmlResponse
from cs.items import CsparserItem
from scrapy.loader import ItemLoader


class CsSpider(scrapy.Spider):
    name = 'castorama'
    allowed_domains = ['castorama.ru']


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://www.castorama.ru/catalogsearch/result/?q={kwargs.get('query')}"]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath('//a[@class="product-list-show-more__link js-product-list-show-more"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@class='product-card__img-link']")
        for link in links:
            yield response.follow(link, callback=self.parse_ads)


    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=CsparserItem(), response=response)
        loader.add_xpath('name', '//h1[@itemprop="name"]/text()')
        loader.add_xpath('price', "//span[@class='price']/span/span/text()")
        loader.add_xpath('photos', '//span[@itemprop = "image"]/@content')
        loader.add_xpath('specs', '//div//*[contains(@class, "specs-table__attribute")]/text()')
        loader.add_value('url', response.url)
        yield loader.load_item()

