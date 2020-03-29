import scrapy
from ..items import LivesourcecrawlItem


class LiveStreamSpider(scrapy.Spider):
    name = "Live_Stream_Spider"

    allowed_domains = ["ivi.bupt.edu.cn/"]
    base_url = "http://ivi.bupt.edu.cn/"
    start_urls = ["http://ivi.bupt.edu.cn/"]

    def parse(self, response):
        channels_list = response.xpath("//div[contains(@class, '2u')]")
        for channel_item in channels_list:
            item_m3u = LivesourcecrawlItem()

            title = channel_item.xpath("./p/text()").extract_first()
            url = channel_item.xpath("./a[2]/@href").extract_first()

            if title and url:  # to pass the pages header title item
                item_m3u["title"] = title
                item_m3u["url"] = url

                yield item_m3u
