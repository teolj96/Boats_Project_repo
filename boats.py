import scrapy


class BoatsSpider(scrapy.Spider):
    name = 'boats'
    allowed_domains = ['www.boat24.com']
    start_urls = ['https://www.boat24.com/uk/secondhandboats/']

  #  custom_settings = {
  #      'DOWNLOAD_DELAY': 15,
  #   }

    def parse(self, response):
        for link in response.css('div.blurb ::attr(data-link)'):
            yield response.follow(link.get(), callback=self.parse_boats)

        next_page = response.css('div.pagination span.link.js-link.pagination__next::attr(data-link)')
        if next_page is not None:
            yield response.follow(next_page.get(), callback=self.parse)

# MAIN PARSER, PARSER THE BOAT INFO

    def parse_boats(self, response):
        boats = response.css('div.l-grid')

        # KEYS THAT I WANT TO USE
        used_spec_keys = ('Year Built', 'Condition', 'Length x Width', 'Material', 'Certified No. of Persons', 'No. of Cabins', 'No. of Beds', 'Propulsion', 'Engine', 'Engine Hours')

        # BOAT SPECIFICATION CSS
        specs = boats.css('div#specs')
        lists = specs.css('ul.list')

        # ITERATE THROUGH KEY LIST AND VAL LIST TO MAKE A DICT OF THE ITEMS
        res = {}
        for i in lists:
            val = i.css('span.list__value::text').getall()
            key = i.css('span.list__key::text').getall()

            for x in key:
                for z in val:
                    res[x] = z
                    val.remove(z)
                    break

        # ITERATE THROUGH THE RES DICT BUT FILTER ONLY THOSE ITEMS THAT I NEED
        res_cleaned = {k:v for k, v in res.items() if k.startswith(used_spec_keys)}

        # SCRAPE THE BOAT MODEL
        res_cleaned['Model'] = boats.css('h1.heading__title::text').get()

        # SCRAPE THE BOAT TYPE
        res_cleaned['Type'] = boats.css('p.heading__title-header a::attr(title)').get()

        # SCRAPE THE LOCATION
        location_1 = response.css('div.l-grid.l-grid--main-side p.text::text').get()

        # TO MAKE IT EASIER I ONLY CHOSE THE LOCATION WHICH HAS THE SYMBOL IN IT
        # BECAUSE A LOT OF THEM HAVE IT
        if '»' in location_1:
            res_cleaned['Location'] = location_1
        else:
            res_cleaned['Location'] = 'Location not available'

        # LIKE FOR LOCATION, SAME FOR PRICE
        price_1 = boats.css('div.contact-box__price-section p.contact-box__price strong::text').get()
        price_2 = boats.css('div.contact-box__price-section p.contact-box__price-type::text').get()

        try:
            if price_1.startswith(('£', 'apx. £')):
                res_cleaned['Price'] = price_1
            elif price_2.startswith(('£', 'apx. £')):
                res_cleaned['Price'] = price_2
            else:
                res_cleaned['Price'] = 'Price not available'
        except:
            res_cleaned['Price'] = 'Price not available'

        yield res_cleaned
