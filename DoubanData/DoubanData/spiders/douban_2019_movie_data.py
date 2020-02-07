# -*- coding: utf-8 -*-
import scrapy
import json
import time
from DoubanData.items import DoubanDataItem2019



class Douban2019MovieDataSpider(scrapy.Spider):
    name = 'douban_2019_movie_data'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/ithil_j/activity/widget/980']

    def __init__(self):
        # 暂时不统计的数据：1047, 1064, 1091
        self.url_num = [963, 986, 1072, 1081, 972, 973, 976, 977, 978, 1086, 1087, 950]

    def parse(self, response):

        # print(response.request.headers['User-Agent'])
        data = json.loads(response.body.decode('utf-8'))
        kind_num = data['res']['kind']
        if kind_num == 1 or kind_num == 28:
            movie_type = data['res']['payload']
            # item = DoubanMovieType()
            type = movie_type['subtitle'] + movie_type['title']
            # item['movie_type'] = type
            #
            # yield item

            subjects = data['res']['subjects']
            for subject in subjects:
                item = DoubanDataItem2019()
                item['movie_url'] = subject['m_url']
                item['movie_orig_name'] = subject['orig_title']
                item['movie_rate'] = subject['rating']
                item['movie_name'] = subject['title']
                item['movie_type'] = type
                yield item


        elif kind_num == 25:
            # print("这儿有运行！！--------------------------------")
            widgets = data['res']['payload']['widgets']
            for widget_type in widgets:
                movie_type = widget_type['payload']
                # item = DoubanMovieType()
                type = movie_type['subtitle'] + movie_type['title']
                # item['movie_type'] = type
                #
                # yield item

                subjects = widget_type['subjects']
                for subject in subjects:
                    item = DoubanDataItem2019()
                    item['movie_url'] = subject['m_url']
                    item['movie_orig_name'] = subject['orig_title']
                    item['movie_rate'] = subject['rating']
                    item['movie_name'] = subject['title']
                    item['movie_type'] = type

                    yield item

        '''
        elif kind_num == 26:
            widgets = data['res']['payload']['widgets']
            for widget_type in widgets:
                people_data = widget_type['payload']
                item = DoubanDataItem2019()
                item['type_title'] = people_data['subtitle'] + people_data['title']

                yield item

                peoples = widget_type['people']
                for people in peoples:
                    item = DoubanDataItem2019()
                    item['people_name'] = people['name']
                    item['people_en_name'] = people['name_en']
                    item['people_profession'] = people['profession']
                    item['people_presentation'] = people['url']

                    yield item
        '''

        i = self.url_num.pop(0)
        next_url = 'https://movie.douban.com/ithil_j/activity/widget/' + str(i)
        print(next_url)
        yield scrapy.Request(next_url, callback=self.parse)

        # yield items
