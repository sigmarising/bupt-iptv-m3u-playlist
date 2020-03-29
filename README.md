# BUPT-IPTV M3U PLAYLIST

BUPT-IPTV is a very popular site among universities in China. You can go through this [site](http://tv.byr.cn/show) with ipv6 support.

But ipv6 hasn't been popularize until today in most place. For these ipv4 only areas, there is still a way to enjoy the BUPT-IPTV by visiting this [site](http://ivi.bupt.edu.cn/).

This ipv4 site provides PC and mobile methods to watch the tv stream:
* PC Methods: there is a `player.html` to get the stream. If you use browser dev tools (in network panel), you can find that the live stream is the same as mobile methods.
* Mobile Methods: directly provide you with a live stream url address, which can be handled correctly by mobile browser.

So we have the chance to make a m3u palylist. And you can use your favorite Video Player to watch the BUPT IPTV in ipv4 environment.

## The Struct of This Project

* `BUPT_IPTV.m3u`: The playlist which you can download directly.
* `utils\`: contains two python program to crawl the live stream address and convert it to m3u list.

## The WorkFlow

1. Use [Scrapy Spider Program](./utils/LiveSourceCrawl) to crawl the live stream url address and save as json file.
2. Use [Convert Script](./utils/ConvertHandler) to convert the json file to m3u file.
3. *(Optional)* Manually add some comments in m3u file.

For detial using the two programs, go to their README pages.