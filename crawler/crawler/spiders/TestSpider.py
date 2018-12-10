from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import re
import json

global visited_links
global data
visited_links = []
data = {}

class MySpider(Spider):
  name = "test_crawler"
  start_urls = ["http://www.cs.put.poznan.pl/mkadzinski/ezi/dzienne/lab10/test/a.html"]

  def parse(self, response):
    global visited_links
    global data
    hxs = Selector(response)
    url = response.url

    print('Starting to process url: ' + url + '\n\n')

    page_name = response.url.split("/")[-1]
    with open("test/" + page_name, 'wb') as f:
      f.write(response.body)

    page = page_name.split(".")[0]
    

    links = hxs.xpath('//a/@href').extract()
    # link_validator = re.compile("^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")

    if url in data:
      pass
    else:
      data[url] = links

    for to_process in links:
      link = to_process

      if not link in visited_links:
        print('processing link: ' + link)
        visited_links.append(link)
        # data[page].append(link)

        yield Request(link, callback=self.parse)
      
  def closed(self, reason):
    print('closed')
    with open("test/" + "result.json", 'w') as f:
      json.dump(data, f)
