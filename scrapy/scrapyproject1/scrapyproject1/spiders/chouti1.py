# -*- coding: utf-8 -*-
import scrapy
import   sys,os,io
from   scrapy.http.response.html import   HtmlResponse
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
##格式问题，当遇到输出前提格式的时候，就可以加上这句

# from    scrapyproject1.scrapyproject1.items import     Scrapyproject1Item
##导入item对象,导入是从当前的目录下面去找

from  ..items import Scrapyproject1Item

class ChoutiSpider(scrapy.Spider):
    name = 'chouti1'
    allowed_domains = ['chouti.com']
    start_urls = ['http://www.chouti.com']

    def parse(self, response):
        print('输出结果如下')

        print(response.request.url)##拿到当前访问的url
        print(response.request.meta.get('depth'))##拿到当前的深度

        # print(response,type(response))
        # print(response.text)
        # print(response.cookies)
        ##//是找孙子，前面可以很多标签，但是找这个bogy下面的孙子有这个属性的,/
        '''
        extra拿到的是文本
        xpath拿到的是对象，可以继续往下面找标签
        //是孙子,子子孙孙，都可以找到
        /是孩子
        @是找属性
        .是在当前的标签下面往下找
        extra_first()只取第一个值 
        ./儿子（当前标签下面）
        .//当前标签下面的孙子
        extarct_first()拿到当前标签下面的第一个文本内容
        extract()拿到所有的标签文本的内容
        *代表任意的标签
        取当前标签下面的属性和文本：
        /text()取当前标签的文本内容
        /@href拿到当前的属性
        response.xpath('//a[2]')
        ##后面的2是按索引来找到第二个
        response.xpath('//a[@href][@id]')是多个条件进行筛选
        //a[contains(@href,"link")]包含的关系，只有这个标签里面delink有这个字段就可以了，后面也可以是其他字符，比如sina 
        //a[start-with(@href,'link')]找到这个属性是否是以link开头的
        re:正则
        //a[re:test(@id,'i\d+')]更高级的用法，前面是固定的写法，后面是找到id属性，后main是匹配的规则，id=i1或id=i2>>>>d+是匹配数字
        //a[re:test(@id,'i\d+')]/text()拿文本，或者其他
        *是匹配多个的写法
        '''
        # content_li=response.xpath('//div[@id="content-list"]/div[@class="item"]')##找到父类还要继续往下找，拿到子类,才可以循环拿到下面的值出来
        content_li=response.xpath('//div[@class="content-list"]/div[@class="item"]')##找到父类还要继续往下找，拿到子类,才可以循环拿到下面的值出来
        # print(response.xpath('//*[@id="newsContent23123186"]//div[1]').extract_first())##去浏览器里面拿到当前的标签，有xpath
        for  item  in  content_li:
            # print(type(item))##对象
            # print(item)#拿到的是对象，可以取里面的值

            # print(item.xpath('./div[@class="news-pic"]').extract_first())##取当前整个的子子孙孙找
            # print(item.xpath('.//a/text()').extract_first())##取当前整个的子子孙孙找，如果是孙类的话，就要//，如果是子类的话，就是/
            item1=item.xpath('.//a/text()').extract_first().strip()##取当前整个的子子孙孙找，如果是孙类的话，就要//，如果是子类的话，就是/
            # print(item1)
        page_list=response.xpath('//div[@id="dig_lcpage"]//a[@class="ct_pagepa"]/@href').extract()
        for  page  in  page_list:
            # f=open('new_log',mode='a+')
            page_url='https://dig.chouti.com/'+page
            # print(page_url)
            # print(response.text)
            # f.write('内容:' + response.text.strip() + '\n')
            from   scrapy.http  import Request
            # print('分页操作')
            from   ..dupliter import  Self_Dupliter
            yield   Request(url=page_url, callback=self.parse,dont_filter=False)##每一次requets的时候，就会执行去重的方法,不准询去重规则，如果要遵循的话，那么应该为false
            # yield   Scrapyproject1Item(url_title=page_url,text=response.text)

            # yield   Request(url=page_url,callback=self.parse)##循环发送请求,循环取这个数据，取执行这个请求,注明一下，callback是执行回调函数，yield，循环执行
            # f.close()
        # print(page_list)

'''
//*[@id="newsContent23123186"]/div[1]
#newsContent23123186 > div.part1 > a.n2
split('',)切割
strip()去除空格
'''