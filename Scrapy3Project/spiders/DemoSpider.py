#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2017/7/14 17:26
# @Author    : 张慧俊[zhanghuijun@souche.com]
# @CopyRight : DataTeam @ SouChe Inc
# @Desc      : 此处用于替换,无特殊说明请删除
import scrapy
from scrapy.cmdline import execute


class DemoSpider(scrapy.Spider):
    name = "demo"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'demo-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log.info('Saved file %s' % filename)


if __name__ == '__main__':
    execute('scrapy crawl demo'.split(' '))
