# coding=utf-8
# !/usr/bin/python
import sys
import requests
from bs4 import BeautifulSoup
import re
from base.spider import Spider
import random
import os
import zipfile
import requests

target_dir2 = "/storage/emulated/0/TV"

if not os.path.exists(target_dir2):
    os.makedirs(target_dir2)

urls = ['.quark','.uc']

for url in urls:
    file_name = url
    save_path = f"{target_dir2}/{file_name}"    
    response = requests.get('https://9071.kstore.vip/jar/' + url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

class Spider(Spider):

    def getName(self):
        return "首页"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeVideoContent(self):
        videos = []

        video = {
            "vod_id": '',
            "vod_name": '更新完成',
            "vod_pic": 'https://imgs-ali.51miz.com/vcg/image/without_watermark/VCG41N512631960.jpg?x-oss-process=image/sharpen,100',
            "vod_remarks": '更新完成!'
        }
        videos.append(video)

        result = {'list': videos}
        return result

    def homeContent(self, filter):
        pass

    def categoryContent(self, cid, pg, filter, ext):
        pass

    def detailContent(self, ids):

        pass

    def playerContent(self, flag, id, vipFlags):
        pass

    def searchContent(self, key, quick):
        return self.searchContentPage(key, quick, '1')

    def searchContentPage(self, key, quick, page):
        pass

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None