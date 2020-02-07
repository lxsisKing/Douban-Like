# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from data_integration import models


class DoubanDataItem2019(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # type_title = scrapy.Field()
    #
    # m_url = scrapy.Field()
    # orig_title = scrapy.Field()
    # rating = scrapy.Field()
    # title = scrapy.Field()
    #
    # people_name = scrapy.Field()
    # people_en_name = scrapy.Field()
    # people_profession = scrapy.Field()
    # people_presentation = scrapy.Field()
    django_model = models.MovieData2019


class DoubanDataItem2018(DjangoItem):
    # type_title = scrapy.Field()
    #
    # m_url = scrapy.Field()
    # orig_title = scrapy.Field()
    # rating = scrapy.Field()
    # title = scrapy.Field()
    #
    # people_name = scrapy.Field()
    # people_en_name = scrapy.Field()
    # people_profession = scrapy.Field()
    # people_presentation = scrapy.Field()
    django_model = models.MovieData2018


