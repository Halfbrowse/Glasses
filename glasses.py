# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):

        for product in response.xpath("//div[@id='product-lists']/div"):
            yield{
                'product_url': product.xpath(".//div[@class='p-title']/a/@href").get(),
                'product_img': product.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@src").get(),
                'product_price': product.xpath(".//div[@class='p-price']/div/span/text()").get(),
                'product_name': product.xpath("normalize-space(.//div[@class='p-title']/a/text())").get()
            }

            next_page = response.xpath(
                "//ul[@class='pagination']/li[position()=last()]/a/@href").get()

            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse)
