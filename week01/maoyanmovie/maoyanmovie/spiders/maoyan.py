# -*- coding: utf-8 -*-
import scrapy, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem as mi


class MaoyanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        Cookie = '__mta=121074487.1593314012121.1593327622093.1593331768016.21; uuid_n_v=v1; uuid=58388340B8ED11EAB4E28FB161D5B82B53B517EE1BF14DA38E44381DC9DDCC66; _csrf=20c3b79955c0d420076677477ff00096ebae2c77a7f0f4353a31719c7a7dee50; _lxsdk_cuid=172f8ea6aa1c8-0d64eceef87b8d-f7d123e-e1000-172f8ea6aa1c8; _lxsdk=58388340B8ED11EAB4E28FB161D5B82B53B517EE1BF14DA38E44381DC9DDCC66; mojo-uuid=1179dfe44c63d65f6d826d03a3bca20d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593325783,1593327399,1593334552,1593346306; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593430641; __mta=121074487.1593314012121.1593331768016.1593430641372.22; _lxsdk_s=17309bbb625-ffc-19c-6c1%7C%7C1'
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, cookies=Cookie ,callback=self.parse, dont_filter=False)

    # 解析函数
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        print(1)
        for movie in movies[:10]:
            item = mi()
            item['movie_title'] = movie.xpath('./div[1]/span/text()').extract()
            item['movie_type'] = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
            item['release_date'] = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip()
            print(item['movie_title'])
            print(item['movie_type'])
            print(item['release_date'])
            yield item