import scrapy


class JumiaSpinder(scrapy.Spider):
    """
    This is a simple crawler for the clothing page of jumia sporting goods page.
    It uses CSS selectors and xpath to extract the name of a product, the rating and the price
    and image source
    """
    name = 'jumia_spider.'
    start_urls = ['https://www.jumia.cm/en/sporting-goods/']

    def parse(self, response):
        for good in response.css('a.link'):
            name = good.css('span.name::text').get()
            price = good.xpath('div/span/span/span/text()').get()
            rating = good.css('.total-ratings::text').get()
            img_src = good.css('.lazy::attr("data-src")').getall()
            if rating:
                "Ratings on jumia are like this:'(5)'. So I trim the first and last bracket"
                rating = rating[1:-1]

            yield {'name': name, 'price': price, 'rating': rating, 'image_src': img_src}

        next_page = response.css('li.item > a::attr("href")').extract()
        print("Next page", next_page)

        for next_link in response.css('li.item > a'):
            yield response.follow(next_link, self.parse)

