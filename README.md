# scrape-sites
-------------

This project contains two spiders for crawling the sites 'https://www.digitalrenter.com/en/search'
and 
https://www.jumia.cm/en/sporting-goods/


The tool used here is [Scrapy](https://scrapy.org/) library. It simply walks the page and 
gets each product and yields its **price, rating, image source and name**.

The main files to check are located in [jumia_shopping.py](./spiders/jumia_shopping_spider.py) and [digital_renter_scrapper.py](./spiders/digital_renter_scrapper.py)

The DigitalRenterSpider spider https://digitalrenter.com for houses and returns house information with the following
price,views,location,type,link.

The JumiaSpider spider crawls https://www.jumia.cm/en/sporting-goods/ for sporting goods

It is a starter project. Ignore the `items.py, middlewares.py, pipelines.py` files and 
concentrate on the files in spiders folder

# Running the project
---------------
You need to install [Scrapy](https://scrapy.org/)  in a virtual environment and 
start a project with the command `scrapy startproject project_name`, my project in this case is Scrappers.
The spider is run from within the spider directory with the command `scrapy runspider jumia_shopping_spider.py`
You should see the jumia.jl file generated. 

The other way for running and generating the results is by running `scrapy crawl digital_renter -o digital_renter.csv` or `scrapy crawl digital_renter -o digital_renter.json`
or `scrapy crawl digital_renter -o digital_renter.xml` to generate for the various file extensions

# Results
----

The generated results for digital renter can be seen in the spiders folder in json, xml and csv.
There are chances for duplicate data so its left for another time for modifications

# How to

You need to inspect a webpage to see the pattern of how the items are.



