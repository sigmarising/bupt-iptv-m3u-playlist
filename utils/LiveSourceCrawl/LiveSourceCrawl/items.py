# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LivesourcecrawlItem(scrapy.Item):
    # the channel's item info

    title = scrapy.Field()  # the Channel's name
    url = scrapy.Field()  # the Channel's live hls url
