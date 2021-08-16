import json
import requests
import datetime
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
			# give more constraints on time frame

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

		today = datetime.datetime.today()
		yesterday = today - datetime.timedelta(days=1)
		yesterday = datetime.datetime.strftime(yesterday, "%Y-%m-%d")
		self.data = {"_lastUpdated": "lt" + yesterday}
		r = requests.get(self.base_url, headers=self.PARAMS, params=self.data)
		return r.json()

	def getDailyData(self):
		today = datetime.datetime.today()
		yesterday = today - datetime.timedelta(days=1)
		yesterday = datetime.datetime.strftime(yesterday, "%Y-%m-%d")
		self.data = {"_lastUpdated":"ge" + yesterday}
		r = requests.get(self.base_url, headers = self.PARAMS, params=self.data)
		return r.json()

	def getCSVData(self):
		today = datetime.datetime.today()
		today = datetime.datetime.strftime(today, "%Y-%m-%d")
		self.data = {"date":"ge" + today}
		r = requests.get(self.base_url, headers=self.PARAMS, params=self.data)
		return r.json()