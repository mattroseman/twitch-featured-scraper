import scrapy


class TwitchSpider(scrapy.Spider):
    name = 'twitch-spider'
    start_urls = [
        'https://twitch.tv',
    ]

    def parse(self, response):
        pass
