__author__ = 'ahmed'
from base import BaseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class ArstechnicaSpider(BaseSpider):
    name = "arstechnica"
    allowed_domains = ["arstechnica.com"]
    start_urls = (
        'http://arstechnica.com/',
    )
    rules = (
        # # Rules should allow only pages will be craweled
        Rule(LinkExtractor(allow=('http://arstechnica.com/([^/\.]+)/\d+/\d+/([^/\.]+)/?$'), unique=True),
             callback='parse_article'),
        # # rules to allow categories only
        Rule(LinkExtractor(allow=('http://arstechnica.com/([^/\.]+)(/page/\d+)?/?$'), unique=True)),
    )


    xpaths = {
        'title': '//h1[@itemprop="headline"]//text()',
        'sub_title': '//h2[@itemprop="description"]//text()',
        'author': '//a[@rel="author"]/span[@itemprop="name"]//text()',
        'image': [
            '//div[@itemprop="articleBody"]//figure[contains(@class,"intro-image")]//img/@src',
            '//div[@itemprop="articleBody"]//figure[contains(@class,"image")]//img/@src',
            '//*[@class="gallery-thumbs"]/li/a/@data-orig'
        ],
        'content': '//div[@itemprop="articleBody"]//p/text()',
        'category' : '//h1[@id="archive-head"]//span',
        'time': '//p[@itemprop="author creator"]//span[@class="date"]/@data-time'
    }