import json
import requests
from auth import getToken

class getData():

	def __init__(self, resource):
		self.base_url = "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/"
		self.resource = resource
		self.base_url = self.base_url + self.resource
		auth = getToken()
		self.token = auth.getToken()
		self.PARAMS = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
                          'Cache-Control': 'no-cache',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'Bearer ' + self.token }


	def getData(self):
		r = requests.get(self.base_url, headers=self.PARAMS)
		return r.json()
