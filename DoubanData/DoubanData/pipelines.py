# -*- coding: utf-8 -*-


# from openpyxl import Workbook


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanDataPipeline(object):

    # def __init__(self):
        # self.wb = Workbook()
        # self.ws = self.wb.active
        # self.i = 0

    def process_item(self, item, spider):
        # 通过爬虫名来判断为哪个爬虫爬取的数据，以方便进行不同形式的存储。
        if spider.name == 'douban_2019_movie_data':  # 处理2019爬虫爬取的数据
            # 通过item.save()将数据直接存入通过django模板创建的数据库表中。
            item.save()
            '''
            # 以下为不与django结合的情况下如何存储数据
            if len(item) == 1:  # 判断该条数据为电影类别还是电影详细信息
                movie_type = [item['type_title']]

                if movie_type is not None:
                    self.ws.append(movie_type)
                    self.i += 1

            if len(item) == 4:

                if 'title' in item:  # 插入相关电影信息
                    movie_line = [item['title'], item['rating'], item['orig_title'], item['m_url']]
                    self.ws.append(movie_line)
                if 'people_name' in item:  # 插入相关人物信息
                    people_line = [item['people_name'], item['people_en_name'], item['people_profession'],
                                   item['people_presentation']]
                    self.ws.append(people_line)

                # 每传过来11条数据就插入空行
                self.i += 1
                if self.i == 11:
                    self.ws.append([])
                    self.i = 0

            self.wb.save('2019-movie-rank-data.xlsx')
            '''

        if spider.name == 'douban_2018_movie_data':
            item.save()
            '''
            if len(item) == 1:  # 判断该条数据为电影类别还是电影详细信息
                movie_type = [item['type_title']]

                if movie_type is not None:
                    self.ws.append(movie_type)
                    self.i += 1

            if len(item) == 4:

                if 'title' in item:  # 插入相关电影信息
                    movie_line = [item['title'], item['rating'], item['orig_title'], item['m_url']]
                    self.ws.append(movie_line)
                if 'people_name' in item:  # 插入相关人物信息
                    people_line = [item['people_name'], item['people_en_name'], item['people_profession'],
                                   item['people_presentation']]
                    self.ws.append(people_line)

                # 每传过来11条数据就插入空行
                self.i += 1
                if self.i == 11:
                    self.ws.append([])
                    self.i = 0

            self.wb.save('2018-movie-rank-data.xlsx')
            '''
        return item
