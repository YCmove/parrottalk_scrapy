import scrapy


class ParrotSpider(scrapy.Spider):
    name = "parrot"

    def start_requests(self):
        url = 'https://www.parrottalks.com/'
        tag = getattr(self, 'tag', None)
        self.logger.info("testing!!!!")
        if tag is not None:
            url = url + 'tag/' + tag
        self.logger.info("url: {}".format(url))
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            self.logger.info("quote: {}".format(quote))
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        