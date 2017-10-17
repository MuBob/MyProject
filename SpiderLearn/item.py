import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author=scrapy.Field()
    chapter=scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()
