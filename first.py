import json
import requests
from auth import getToken
from resources import resources

class getData():

	def __init__(self, resource, auth):

		#auth = getToken()
		#self.token = auth.getToken()
		self.token = auth
		if resource == 'Slot':
			self.base_url = "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Slot"
			self.data = {'appointment-type':877} # will need to make more of these, for all appointment types in prod

		else:
			self.base_url = "https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/"
			self.resource = resource
			self.base_url = self.base_url + self.resource
			self.data = None

		self.PARAMS = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
					   'Cache-Control': 'no-cache',
					   'Content-Type': 'application/x-www-form-urlencoded',
					   'Authorization': 'Bearer ' + self.token}



	def getData(self):
		r = requests.get(self.base_url, headers=self.PARAMS, params=self.data)
		return r.json()
