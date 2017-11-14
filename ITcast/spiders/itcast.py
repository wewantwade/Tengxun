# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    #启动爬虫是必须的参数
    name = 'itcast'
    #爬虫域的范围
    allowed_domains = ['itcast.cn']
    #爬虫执行后第一批请求将从这个列表获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    #解析网页响应
    def parse(self, response):
        node_list=response.xpath("//div[@class='li_txt']")
        for node in node_list:
            #创建item字段对象，用来存储信息
            item=ItcastItem()
            #xpath返回的是一个列表，用[0]取出数据
            #.extract()将xpath对象转换为unicode字符串
            name=node.xpath("./h3/text()").extract()#text()是取出内容，此时是一个xpath对象而不是文本，然后用extract()转成文本
            title=node.xpath("./h4/text()").extract()
            info=node.xpath("./p/text()").extract()

            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]

            yield item
        # print(response.body.decode('utf-8'))

