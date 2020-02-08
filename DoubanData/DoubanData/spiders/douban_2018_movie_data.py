# -*- coding: utf-8 -*-
import scrapy
import json
import time
from DoubanData.items import DoubanDataItem2018


class Douban2018MovieDataSpider(scrapy.Spider):
    name = 'douban_2018_movie_data'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/ithil_j/activity/movie_annual2018/widget/1']

    def __init__(self):
        # 暂时不处理的数据： 62, 63, 64
        self.url_num = [2, 4, 5, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 31, 33, 34, 36, 37, 38,
                        40, 41, 43, 44, 46, 47, 48, 53, 54, 55, 56, 57, 59, 60]

    def parse(self, response):
        # 由于该页面为json数据存储，所以加载后直接获取
        data = json.loads(response.body.decode('utf-8'))
        kind_num = data['res']['kind']
        if kind_num == 1:
            movie_type = data['res']['payload']
            # item = DoubanMovieType()
            # item['movie_type'] = movie_type['title']
            #
            # yield item

            subjects = data['res']['subjects']
            for subject in subjects:
                item = DoubanDataItem2018()
                item['movie_url'] = subject['m_url']
                item['movie_orig_name'] = subject['orig_title']
                item['movie_rate'] = subject['rating']
                item['movie_name'] = subject['title']
                item['movie_type'] = movie_type['title']
                # 将爬取到的信息传到管道进行处理
                yield item
                time.sleep(0.2)

        '''
        # 暂时先不处理人物数据

        if kind_num == 4:
            people_data = data['res']['payload']
            item = DoubanDataItem2018()
            item['type_title'] = people_data['title']

            yield item

            peoples = data['res']['people']
            for people in peoples:
                item = DoubanDataItem2018()
                item['people_name'] = people['name']
                item['people_en_name'] = people['name_en']
                item['people_profession'] = people['profession']
                item['people_presentation'] = people['url']

                yield item
        '''

        # 组建下一页需要爬取的内容
        i = self.url_num.pop(0)
        next_url = 'https://movie.douban.com/ithil_j/activity/movie_annual2018/widget/' + str(i)
        print(next_url)
        # 通过yield使用request方法对下一个url进行数据提取。回调函数为self.parse本身
        yield scrapy.Request(next_url, callback=self.parse)
