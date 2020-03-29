# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import colorama as c


class LivesourcecrawlPipeline(object):
    items_list = []
    output_file = "./channels.json"
    base_url = "http://ivi.bupt.edu.cn"

    def open_spider(self, spider):
        # init colorama
        c.init(autoreset=True)
        print(c.Fore.GREEN + c.Style.BRIGHT + "- CRAWLING START -")

    def close_spider(self, spider):
        # save list in file and close colorama
        print(c.Fore.GREEN + c.Style.BRIGHT + "- CRAWLING DONE -")

        with open(self.output_file, 'w+', encoding='utf-8') as f:
            json.dump({"channels": self.items_list}, f, ensure_ascii=False, indent=4)

        print(c.Fore.GREEN + c.Style.BRIGHT + "- SAVING DONE -")
        c.deinit()

    def process_item(self, item, spider):
        item_m3u = dict(item)
        print(c.Fore.YELLOW + "  handling: ", end="")
        print(item_m3u["title"])

        # save the item in list
        self.items_list.append({
            "title": item_m3u["title"],
            "url": self.base_url + item_m3u["url"]
        })

        return item
