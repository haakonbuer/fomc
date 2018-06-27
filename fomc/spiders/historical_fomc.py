import scrapy

class HistoricalSpider(scrapy.Spider):
    name = 'historical'

    url_pattern = 'https://www.federalreserve.gov/monetarypolicy/fomchistorical{0}.htm'
    #start_urls = ['https://www.federalreserve.gov/monetarypolicy/fomchistorical1936.htm']
    start_urls = [url_pattern.format(x) for x in range(1936, 2010)]

    def parse(self, response):

        for title in response.css('#article').css('h5::text'):
            yield {'date' : title.extract()}
