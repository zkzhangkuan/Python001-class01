# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
class MaoyanmoviePipeline:
    # def process_item(self, item, spider):
    #     return item

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        movie_title = item['movie_title']
        movie_type = item['movie_type']
        release_date = item['release_date']
        mylist = [movie_title, movie_type, release_date]
        name=['电影名称','类型','上映时间']
        movie1 = pd.DataFrame(columns=name, data = mylist)
        movie1.to_csv('./maoyan_movie.csv', encoding='utf-8', index=False, header=False)
        return item