#coding utf-8
# -*- coding: utf-8 -*-
import  sys
import  time
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from kitchenStories.items import KitchenstoriesItem
import json
import re
class KchenStory_Spider(BaseSpider):
    name="kcs"
    headers = {'Host': 'm.haodou.com',
                'Connection': 'keep-alive',
                'Content-Length': '45',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'http://m.haodou.com',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043128 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/WIFI Language/zh_CN',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'http://m.haodou.com/video/search/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,en-US;q=0.8',
                'Cookie': 'PHPSESSID=0oe5v3vjbjjuilf6ii988gpfg5; Hm_lvt_d401a76b6ac9cc0323ddd3257e4f8b1f=1492611552; Hm_lpvt_d401a76b6ac9cc0323ddd3257e4f8b1f=1492611715'

              }
    def start_requests(self):
        #for page in range(1,25):
             #yield self.make_requests_from_url('http://api.haodou.com/index.php?appid=2&appkey=9ef269eec4f7a9d07c73952d06b5413f&format=json&sessionid=1492570383666&vc=113&vn=6.1.23&loguid=10533315&deviceid=haodou863127037714141&uuid=4c97b7dc74870a0ed417d13052e87753&channel=huawei_v6123&method=Video.searchVideo&virtual=&signmethod=md5&v=3&timestamp=1492592108&nonce=0.2916103797981531&appsign=20d5f02f4ad2c6d2bac6d27c3ecbcc0f') # 开始抓取
        #按实物的名称进行抓取需要读取种子文件
        #------------------------------------------------
        file_object = open('haodouzhongzi.txt', 'r')
        try:
            for line in file_object:
                for page in range(1,26):
                    yield Request('http://m.haodou.com/video/ajax/?type=search&keyword='+line+'&page='+str(page),callback=self.parse3)
        finally:
            file_object.close()
            #------------------------——-------------------------------------
            # years_object.close()
        #yield Request('http://m.haodou.com/video/ajax/?type=search&keyword=%E7%B1%B3%E9%A5%AD&page=1',callback=self.parse3)# 按食物的名称进行抓取//进行扩展
        #yield Request('http://m.haodou.com/video/ajax/?type=search&keyword=%E7%B1%B3%E9%A5%AD&page=1',callback=self.parse2)  # 按食物种类进行抓取
        #yield Request('http://m.haodou.com/video/cate/',callback=self.parse1)  # 按食物种类进行抓取

    def parse1(self,response):
        hxs = Selector(response)
        #item = KitchenstoriesItem()
        catgorylist=hxs.xpath('/html/body/div/div[2]/div/ul/li');
        for li in catgorylist:
            url=li.xpath('a/@href').extract()[0]
            catname=li.xpath('a/text()').extract()[0]#种类名称
            catid=url.split('=',1)[1]#提取出种类id
            #print catid[1]
            #print text
            #item =KitchenstoriesItem()#持久hua
            #item['catid']=catid[1]
            #item['catname']=text
            for page in  range(1,26):
                yield Request('http://m.haodou.com/video/ajax/?type=catevideo&_type=1&cate_id='+catid+'&page='+str(page),meta={'catid':catid,'catname':catname},callback=self.parse2)  # 按食物种类进行抓取



    def parse2(self,response):

        #print "123"+response.meta['text']+'-----id='+response.meta['catid'];
        #item = KitchenstoriesItem()
        #item['catid'] = '1122'
        #item['catname']='1123'
        #item = response.meta['item']
        catid=response.meta['catid']
        catname=response.meta['catname']
        hxs=json.loads(response.body_as_unicode())
        hx1=hxs['result']
        hx2=hx1['html']
        # 正则表达式提取内容
        #if(hx2.)
        myItems = re.findall(r'<li>(.*?)</li>', hx2, re.S|re.M)
        #lenmyItems=len(myItems)
        for line in myItems:
              #print line
              item = KitchenstoriesItem()
              src=re.findall(r"(?<=src=\").+?(?=\")|(?<=href=\').+?(?=\')",line,re.I|re.S|re.M)
              #print src[0]
              #video=re.match('.*/recipe/l/(.*)_(\w+.jpg)',src[0]).group(1)
              video = re.match('.*/recipe/l/(.*)_(\w+.jpg)', src[0])
              videosourceurl=video.group(1)
              videourl='http://m.haodou.com/recipe/'+videosourceurl.split('/',2)[2]+'/'
              ngnixurl='http://120.25.213.154/img/video/'+videosourceurl.split('/',2)[2]+'.mp4'
              item['imgurl']=src[0]
              #item['videourl']='http://v.hoto.cn/'+re.match('.*/recipe/l/(.*)_(\w+.jpg)',src[0]).group(1)+'.mp4'
              item['videosourceurl'] = 'http://v.hoto.cn/' + videosourceurl + '.mp4'
              item['videourl']=videourl
              #title=re.findall(r"<h2 .*?>(.*?)</h2>",line,re.S|re.M)
              item['chinesename']=re.findall(r"<h2 .*?>(.*?)</h2>",line,re.S|re.M)[0]
              item['catid']=catid
              item['catname']=catname
              item['source']='好豆网'
              item['ngnixurl']=ngnixurl
              yield item
              #print title[0]
    def parse3(self,response):

        #print "123"+response.meta['text']+'-----id='+response.meta['catid'];
        #item = KitchenstoriesItem()
        #item['catid'] = '1122'
        #item['catname']='1123'
        #item = response.meta['item']
        #catid=response.meta['catid']
        #catname=response.meta['catname']
        hxs=json.loads(response.body_as_unicode())
        hx1=hxs['result']
        hx2=hx1['html']
        # 正则表达式提取内容
        #if(hx2.)
        myItems = re.findall(r'<li>(.*?)</li>', hx2, re.S|re.M)
        #lenmyItems=len(myItems)
        for line in myItems:
              #print line
              item = KitchenstoriesItem()
              src=re.findall(r"(?<=src=\").+?(?=\")|(?<=href=\').+?(?=\')",line,re.I|re.S|re.M)
              #print src[0]
              #video=re.match('.*/recipe/l/(.*)_(\w+.jpg)',src[0]).group(1)
              video = re.match('.*/recipe/l/(.*)_(\w+.jpg)', src[0])
              videosourceurl=video.group(1)
              videourl='http://m.haodou.com/recipe/'+videosourceurl.split('/',2)[2]+'/'
              ngnixurl='http://120.25.213.154/img/video/'+videosourceurl.split('/',2)[2]+'.mp4'
              item['imgurl']=src[0]
              #item['videourl']='http://v.hoto.cn/'+re.match('.*/recipe/l/(.*)_(\w+.jpg)',src[0]).group(1)+'.mp4'
              item['videosourceurl'] = 'http://v.hoto.cn/' + videosourceurl + '.mp4'
              item['videourl']=videourl
              #title=re.findall(r"<h2 .*?>(.*?)</h2>",line,re.S|re.M)
              item['chinesename']=re.findall(r"<h2 .*?>(.*?)</h2>",line,re.S|re.M)[0]
              item['catid']=''
              item['catname']=''
              item['source']='食品网'
              item['ngnixurl']=ngnixurl
              yield item
              #print title[0]

