#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2017/7/14 17:12
# @Author    : 张慧俊[zhanghuijun@souche.com]
# @CopyRight : DataTeam @ SouChe Inc
# @Desc      : 此处用于替换,无特殊说明请删除

import random
import time

from Scrapy3Project.resource.ResourceHelper import ResourceHelper


class RandomProxyMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://182.37.31.50:809'

    def process_exception(self, request, exception, spider):
        request.meta['proxy'] = 'http://127.0.0.1:8888'


class UserAgentMiddleware(object):
    def __init__(self):
        self.resourceHelper = ResourceHelper()
        self.user_agent_list = self.resourceHelper.loadJson('useragent.json')
        self.uaCache = {}

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers['User-Agent'] = ua

    def process_exception(self, request, exception, spider):
        ua = random.choice(self.user_agent_list)
        request.headers['User-Agent'] = ua
        spider.logger.error('UserAgent Expection:%s' % str(exception))


class LogDownloadMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request, spider):
        spider.logger.debug('[MYLOG] [%s] %s %s %s %s' % (
        'download_request', request.meta.get('retry_times'), request.url, str(request.meta.get('proxy')),
        str(int(time.time() * 1000))))

    def process_exception(self, request, exception, spider):
        spider.logger.debug('[MYLOG] [%s] %s %s %s %s mark:%s' % (
            'download_exception', request.meta.get('retry_times'), request.url, str(request.meta.get('proxy')),
            str(int(time.time() * 1000)),
            str(request.meta.get('_userId', '')) + ',' + str(request.meta.get('userId', '')) + ',' + str(exception)))
