#爬取猫眼电影排行前10名的电影名称、类型及上映时间
import requests, re, csv, time, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from bs4 import BeautifulSoup as bs
import pandas as pd

requests.adapters.DEFAULT_RETRIES = 15

class movie():
    def __init__(self):
        self.url = 'https://maoyan.com/films?showType=3'
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        self.Cookies = '__mta=121074487.1593314012121.1593327622093.1593331768016.21; uuid_n_v=v1; uuid=58388340B8ED11EAB4E28FB161D5B82B53B517EE1BF14DA38E44381DC9DDCC66; _csrf=20c3b79955c0d420076677477ff00096ebae2c77a7f0f4353a31719c7a7dee50; _lxsdk_cuid=172f8ea6aa1c8-0d64eceef87b8d-f7d123e-e1000-172f8ea6aa1c8; _lxsdk=58388340B8ED11EAB4E28FB161D5B82B53B517EE1BF14DA38E44381DC9DDCC66; mojo-uuid=1179dfe44c63d65f6d826d03a3bca20d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593325783,1593327399,1593334552,1593346306; mojo-session-id={"id":"cb5c7539a953ec846a8872ec79965aa2","time":1593354888119}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593354888; __mta=121074487.1593314012121.1593331768016.1593354888217.22; _lxsdk_s=172fb5a1067-2b8-fa2-10%7C%7C3'
        self.header = {'user-agent':self.user_agent,'Cookie':self.Cookies, "Referer":"https://www.maoyan.com/"}

    def get_movie_list(self):
        '''
        获取电影的信息
        '''
        movie_list = []
        response = requests.get(self.url, headers=self.header)
        time.sleep(5)
        bs_info = bs(response.text, 'html.parser')

        for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
            movie_name = tags.div.find('span', attrs={'class': 'name'}).text
            movie_type = None
            release_date = None
            hover_tags = tags.find_all('span', attrs={'class': 'hover-tag'})
            for tag in hover_tags:
                if tag.text == "类型:":
                    movie_type = tag.parent.text.replace(' ', '').replace('\n', '').split(':')[1]
                if tag.text == "上映时间:":
                    release_date = tag.parent.text.replace(' ', '').replace('\n', '').split(':')[1]
            movie_list.append([movie_name, movie_type, release_date])
        return movie_list[:10]

    def data_to_csv(self):
        '''
        把结果存入文件
        '''
        mylist = self.get_movie_list()
        name=['电影名称','类型','上映时间']
        movie1 = pd.DataFrame(columns=name, data = mylist)
        movie1.to_csv('./movie.csv', encoding='utf-8', index=False, header=False)

if __name__ == "__main__":
    movie().data_to_csv()

