"""Scrapes amazon for rankings of books with "Python" in their title."""

import scrapy

class BookSpider(scrapy.Spider):
    """Crawls for books!"""
    name = "py_books"
    start_urls = [
        r"https://www.amazon.com/s/ref=sr_st_relevancerank?keywords=programming+books&rh=n%3A283155%2Cn%3A173507%2Ck%3Aprogramming+books&qid=1490762365&sort=relevancerank"
    ]
    custom_settings = {
        "REDIRECT_ENABLED": False,
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }

    def parse(self, response):
        for book in response.css('li.s-result-item'):
            result = {
                'title': book.css("h2.s-access-title::text").extract_first(),
            }
            if "Python" in result["title"]:
                yield result
        next_page = response.css("#pagnNextLink::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, meta={
                'dont_redirect': True,
            }, callback=self.parse)
