# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetAllItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    JobTitle = scrapy.Field()
    
    Salary=scrapy.Field()

    PushDate=scrapy.Field()

    Position=scrapy.Field()

    Require = scrapy.Field()

    City_address=scrapy.Field()

    Authentication=scrapy.Field()

    TelePhone=scrapy.Field()

    Scale=scrapy.Field()

    Nature=scrapy.Field()

    Address=scrapy.Field()

    Position_intro=scrapy.Field()

    
