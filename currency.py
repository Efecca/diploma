#global
import json
import requests

#project
import settings

class Currency:
    def getRates(self):
        return self.fake()
    
    def online(self):
        info = {'api_key': settings.CURRENCY_API_KEY}
        response = requests.get("http://apilayer.net/api/live", params=info)
        return response.json()

    def fake(self):
        with open('fakeCurrency.json') as f:
            data = json.load(f)

        return data
