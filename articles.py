#global
import json
import eventregistry

#project
import settings

class Articles:
    def getArticles(self):
        return self.fake()
    
    def online(self):
        er = EventRegistry(apiKey = settings.ARTICLES_API_KEY)
        return response.json()

    def fake(self):
        with open('fakeArticles.json') as f:
            data = json.load(f)

        return data
