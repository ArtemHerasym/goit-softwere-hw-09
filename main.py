import scrapy
from scrapy.crawler import CrawlerProcess
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def __init__(self):
        self.quotes_data = []
        self.authors_data = []
        self.authors_seen = set()

    def parse(self, response):
        for quote in response.css("div.quote"):
            quotes = {
                      "tags" : quote.css(".tag::text").getall(),
                      "author" : quote.css(".author::text").get(),
                      "quote" : quote.css(".text::text").get()
                      }
            yield quotes
            author_link = quote.css("a[href^='/author']::attr(href)").get()
            self.quotes_data.append(quotes)
            yield response.follow(author_link, callback=self.parse_author)

        next_page = response.css(".next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):

        authors = {
            "fullname" : response.css(".author-title::text").get(),
            "born_date" : response.css(".author-born-date::text").get(),
            "born_location" : response.css(".author-born-location::text").get(),
            "description" : response.css(".author-description::text").get().strip(),
        }
        fullname = authors["fullname"]
        if fullname not in self.authors_seen:
            self.authors_seen.add(fullname)
            self.authors_data.append(authors)
        yield authors

    def closed(self, reason):
        with open ('quotes.json', 'w', encoding='utf-8') as f:
            json.dump(self.quotes_data, f, indent=2, ensure_ascii=False)

        with open ('authors.json', 'w', encoding='utf-8') as f:
            json.dump(self.authors_data, f, indent=2, ensure_ascii=False)




process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()