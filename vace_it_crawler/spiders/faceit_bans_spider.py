import scrapy
import json

class FaceItBansSpider(scrapy.Spider):
    name = "face_it_bans"
    quotes_base_url = 'https://api.faceit.com/core/v1/bans?limit=%s&offset=%s'
    start_urls = [quotes_base_url % (100, 0)]
    # download_delay = 1.5

    # parse whole HTML
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'face-it-bans-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('payload', []):
            yield {
                '_id': item.get('_id'),
                'reason': item.get('reason'),
                'reason_type': item.get('reason_type'),
                'type': item.get('type'),
                'starts_at': item.get('starts_at'),
                'ends_at': item.get('ends_at'),
                'user_id': item.get('user_id'),
                'nickname': item.get('nickname'),
                'guid': item.get('guid'),
            }
        # if data['has_next']:
        #     next_page = data['offset'] + 1
        #     yield scrapy.Request(self.quotes_base_url % next_page)
