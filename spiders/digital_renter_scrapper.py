import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class DigitalRenterSpider(scrapy.Spider):
    name = "digital_renter"
    start_urls = ["https://www.digitalrenter.com/en/search"]
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@rel="next"]'),
             follow=True,
             callback='parse'),
    )

    def parse(self, response):
        for property in response.css('div.listing-item'):
            link = property.css('.listing-item-link::attr("href")').get()
            type = property.css('div.col-lg-7::text').get().strip()
            location = property.css('span.txt-caps::text').get().strip()
            price = property.css('span.aa-price::text').get().strip()
            views = property.css('div.float-left > span::text').get().strip()
            promo_price = property.css('span.lst-promo-price::text').get()
            if promo_price:
                print(type, location, link, views, "{} {}".format(promo_price.strip(), price))
                yield {'link': link, 'type': type, 'location': location, 'price': "{} {}".format(price, promo_price),'views':views}
                print("----------------------------------------")
            else:
                print(type, location, link, views, price)
                print("----------------------------------------")
            yield {'link': link, 'type': type, 'location': location, 'price': price,'views':views}

        # At the time of writing these, digitalrenter search spans till page 11
        # So let's parse the from page 2 to page 11 and scrap it.
        base = "https://www.digitalrenter.com/en/search?page={}"
        for count in range(2, 12):
            yield response.follow(base.format(count), callback=self.parse)
