# scrape-sites
-------------

This project is a simple spider for crawling 'https://www.jumia.cm/en/sporting-goods/ .

The tool used here is [Scrapy](https://scrapy.org/) library. It simply walks the page and 
gets each product and yields its **price, rating, image source and name**.

The main file to check is located in [jumia_shopping.py](./spiders/jumia_shopping_spider.py)

The settings for the project is done in [settings.py](./settings.py) by setting the feed format
and feed_uri as `jsonlines` and `jumia.jl` respectively. You will see a sample of the crawled data
in [jumia.jl](./spiders/jumia.jl)


# Running the project
---------------
You need to install [Scrapy](https://scrapy.org/)  in a virtual environment and 
start a project with the command `scrapy startproject project_name`, my project in this case is Scrappers.
The spider is run from within the spider directory with the command `scrapy runspider jumia_shopping_spider.py`
You should see the jumia.jl file generated

