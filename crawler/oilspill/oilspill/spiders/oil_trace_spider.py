import scrapy
import csv


class OilTraceSpider(scrapy.Spider):
    name = "oiltrace"

    def start_requests(self):
        urls = [
            'https://g1.globo.com/natureza/noticia/2019/10/08/lista-de-praias-atingidas-pelas-manchas-de-oleo-no-nordeste.ghtml'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        with open('oilstory.csv', 'w') as csv_file:
            wr = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
            for row in response.xpath('//tr'):
                list_row = row.css('td::text').getall()
                wr.writerow(list_row)



