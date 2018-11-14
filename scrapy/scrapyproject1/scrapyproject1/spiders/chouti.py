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

    ##第二种定义代理的方式是自定义代理
    def parse(self, response):
        yield  Request(url='',callback=self.parse,meta={'proxy':'"http://root:xx@192.1.1.1/"'})##通过meta的方式传参数进来
        ##把url放进调度器里面,requets.meta里面，后面的代理url



#########设置代理：httpproxy,内置代理
# import   os
# os.environ['HTTPS_PROXY']='192.1.1.1'##这种方式是在当前的进程下面设置的临时的代理方式，他会写入请求头里面，随着请求提交的时候，一起进行访问，在当前的进程下面有效，在其他进程下面是没有的
# os.environ['HTTPS_PROXY']='http://root:xx@192.1.1.1/'
'''
方式一：环境变量读取代理的方式
在环境变量里面进行设置这个进代理进去，然后在源码里面可以找到
'''

