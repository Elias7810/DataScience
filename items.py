import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def clear_price(value):
    if value:
        value = value.replace(' ','')
        try:
            value = int(value)
        except:
            return value
        return value

def clear_specs(value):
    value = [''.join(el.replace('\n', ' ') for el in value)]
    value = [el.strip() for el in value if el.isspace() == False]
    #Хотел сделать список более читабельным, соединив в одной строке признак и его значение,
    #попарно объединив элементы в списке. Однако почему-то ни одна из команд под комментарием
    #в mapcompose не работает, хотя если их применить независимо, они дают нужный результат.
    #В чем же может быть дело?

    #value = [value[i] + ' - ' + value[i + 1] for i in range(0, len(value), 2)]

    #si = iter(value)
    #value = list(map(' - '.join, zip(si, si)))
    list(range(0, len(value), 2))
    return value


class CsparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(clear_price), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    specs = scrapy.Field(input_processor=MapCompose(clear_specs))
    _id = scrapy.Field()
