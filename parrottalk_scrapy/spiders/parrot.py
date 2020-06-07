import pprint
import json
import scrapy
from scrapy.http import Request, FormRequest
from parrottalk_scrapy import settings

# settings.LOGIN_URL

class ParrotSpider(scrapy.Spider):
    name = "parrot"
    allowed_domains = ['www.parrottalks.com']
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6",
        "content-length": "19",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.parrottalks.com",
        "referer": "https://www.parrottalks.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    payload = {"from": "facebook"}

    def start_requests(self):
        yield scrapy.Request(url=settings.CATELOG_API, method='GET', headers=self.headers, cookies=settings.COOKIES, callback=self.parse
        )

        # yield scrapy.Request(url=settings.LOGIN_API, method='POST', headers=self.headers, body=json.dumps(self.payload), cookies=settings.COOKIES, callback=self.parse
        # )

        # return [Request(settings.LOGIN_URL, meta={'cookiejar': 1}, callback=self.post_login)]
        
        # url = 'https://www.parrottalks.com/'
        # tag = getattr(self, 'tag', None)
        # self.logger.info("testing!!!!")
        # if tag is not None:
        #     url = url + 'tag/' + tag
        # self.logger.info("url: {}".format(url))
        # yield scrapy.Request(url, self.parse)

    def parse(self, response):
        pprint("pprint: ", response)

        # yield scrapy.Request(url='https://www.parrottalks.com/api/catalogs?note_only=1', cookies = settings.COOKIES, callback = self.parse2
        # )
        # self.make_requests_from_url(settings.BOOK_URL)
    #     for quote in response.css('div.quote'):
    #         self.logger.info("quote: {}".format(quote))
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('small.author::text').extract_first(),
    #         }

    #     next_page = response.css('li.next a::attr(href)').extract_first()
    #     if next_page is not None:
    #         yield response.follow(next_page, self.parse)
        
    # def parse2(self, response):
    #     pprint("pprint: ", response)
