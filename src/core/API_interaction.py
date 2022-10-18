from core.config import *
import requests
import json

# API interaction is function to update and get content via rest API of confluence.
# It currently uses for confluence version 7.18 or later
# Reference document:
# https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content/#api-wiki-rest-api-content-get
# https://developer.atlassian.com/server/confluence/confluence-rest-api-examples/
class api_interaction:
    def __init__(self):
        self.confluenceURL = confluenceURL
        self.pageID = pageID
        self.APIkey = APIkey
        self.headers = headers
        self.url = url

    def get(self, custom_URL=url):
        response = requests.request("GET", custom_URL, headers=self.headers)
        return json.loads(response.text)

    def update(self, payloadData):
        payload = json.dumps(payloadData)
        response = requests.request("PUT", self.url, data=payload, headers=self.headers)
        return json.dumps(
            json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
        )
