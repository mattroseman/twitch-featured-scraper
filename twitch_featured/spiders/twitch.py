import scrapy


class TwitchSpider(scrapy.Spider):
    name = 'twitch-spider'
    start_urls = [
        'https://twitch.tv',
    ]

    def parse(self, response):
        streamer = response.xpath('//p[@data-a-target="carousel-broadcaster-displayname"]/text()').extract()
        playing = response.xpath('//p[@data-a-target="carousel-user-playing-message"]/span/a/text()').extract()

        yield {
            'streamer': streamer,
            'playing': playing
        }
