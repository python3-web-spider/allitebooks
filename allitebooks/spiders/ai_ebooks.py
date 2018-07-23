# -*- coding: utf-8 -*-
import scrapy
from allitebooks.items import AllitebooksItem


class AiEbooksSpider(scrapy.Spider):
    name = 'ai_ebooks'
    allowed_domains = ['www.allitebooks.com']
    start_urls = ['http://www.allitebooks.com/']

    def parse(self, response):
        for href in response.css('.entry-title>a::attr(\'href\')'):
            yield response.follow(href, self.parse_detail)

    def parse_detail(self, response):
        item = AllitebooksItem()
        item['title'] = response.css('.single-title::text').extract_first()
        item['author'] = response.css('.book-detail > dl > dd:nth-child(2) > a::text').extract_first()
        item['download_link'] = response.css('span.download-links:nth-child(1) a::attr(\'href\')').extract_first()
        yield item
