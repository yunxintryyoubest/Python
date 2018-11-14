# -*- coding: utf-8 -*-
import scrapy
import   sys,os,io
from   scrapy.http.response.html import   HtmlResponse
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
##格式问题，当遇到输出前提格式的时候，就可以加上这句
from   scrapy.http.request    import  Request
# from    scrapyproject1.scrapyproject1.items import     Scrapyproject1Item
##导入item对象,导入是从当前的目录下面去找

from  ..items import Scrapyproject1Item
from  scrapy.http.cookies import  CookieJar


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://www.chouti.com']
    cookie_dict = {}
    ##深度：
    from scrapy.spidermiddlewares.depth import DepthMiddleware
    ###有一个调度这个parse的方法，是将这个parse生成器》》迭代器，循环取出里面的值出来
    ##返回结果在当前的requets对象里面加1加1


    '''
    在这里可以可以是生成器，或者是可迭代对象（列表），当每yield一次的时候，就执行官start_requets里面的.__next__方法
    在那里将这个生成器转化为了迭代器iter，默认返回对象是parse，每执行一次__next__方法的时候，depth就加1，然后下载优先级就减少
 
    '''
    def parse(self, response):
        print('输出结果如下')
        print(response.meta.get('depth',0))##打印出当前深度出来,默认最开始是0
        cookie_obj=CookieJar()##把cookie解析出来
        cookie_obj.extract_cookies(response,response.request)##得需要一个cookie-jar的对象来获取
        ##response里面有响应体，有响应头，可以去响应体里面获取cookies
        '''
        解析出响应头中的cookies，放到cookie_obj里面
        发送数据的时候，是&的格式进行发送的，data
        如果是json=什么的话，那么就是字典的形式发送过去
        '''
        '''
        发送数据注意：
        如果是json的话，是字典的形式发送过去的
        如果是data的话，那么就是&的形式发送过去的
        '''
        # for  k,v  in cookie_obj._cookies.items():
        #     for  i,j in  v.items():
        #         for  m,n  in  j.items():
        #             self.cookie_dict[m]=n.value
        #
        # from urllib.parse import  urlencode
        # yield   Request(
        #     url='https://dig.chouti.com/login',##发送的url
        #     method='POST',##方法
        #     body='phone=8613237005217&password=192855wang,,..??&oneMonth=1',
        # body=urlencode(
            #         {'phone': 8613237005217,
            #         'password': '192855wang,,..??',
            #         'oneMonth': 1}##&的形式发送
            #
            # ),##请求体，，注明一下，如果是josn的格式的话，那么就是字典的形式，如果是data的话，那么就是&的形式发送过去
    #         cookies=self.cookie_dict,##携带的cookies,ccokie是在你发送过去的时候，就会存进来
    #         headers={
    #             'Content-Type': 'application / x - www - form - urlencoded;charset = UTF - 8',##json，data的类型
    #             'USER_AGENT' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    #
    #     },##请求头，以字典的形式发送过去的,user-angent是可以在settings里面配置的，就不用每一次都加了
    #         callback=self.check_login,
    #     )
    # def  check_login(self,response):
    #     print('suc')
    #     print(response.text)

