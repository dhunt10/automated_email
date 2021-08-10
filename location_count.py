from first import getData
import pandas as pd
import datetime

class locationManager():
    def __init__(self):
        """
	"""

    def getCSVData(self):
        locationNames, locationIds = self.getLocation()
        values = self.getLocationValues(locationIds)
        if len(values) == len(locationNames) and len(locationNames) == len(locationIds):
            df = pd.DataFrame()
            df['location_id'] = locationIds
            df['location_name'] = locationNames
            df['appointment_count'] = values

            #todo this will have to change when transferred to raspberry pi
            df.to_csv('/Users/darinhunt/OnSpot/code/modmed/automated_email/files/file.csv')

    def getLocation(self):
        location_ids = []
        location_names = []

        x = getData('Location').getData()
        for i in range(len(x['entry'])):
            loc = x['entry'][i]['resource']['name']
            id = x['entry'][i]['resource']['id']
            location_ids.append(id)
            location_names.append(loc)
        return location_names, location_ids

    def getLocationValues(self, locations):
        values = []
        appts = getData('Appointment').getData()
        count = 0
        for i in range(len(locations)):
            for j in range(appts['total']):
                if (appts['entry'][j]['resource']['participant'][1]['actor']['reference'].split('/')[-1]) == locations[i] \
                    and (datetime.datetime.strptime(appts['entry'][j]['resource']['start'].replace('T', ' ').split('+')[0], '%Y-%m-%d %H:%M:%S.%f') > datetime.datetime.today()):

                    count = count + 1
            values.append(count)
        return values

    def getIndividualValues(self):

        locationNames = []
        apptDate = []
        appts = getData('Appointment').getData()
        #counts = [1] * len(appts['total'])
        locationMap = self.getLocationZips()

        for i in range(appts['total']):
            if (datetime.datetime.strptime(appts['entry'][i]['resource']['start'].replace('T', ' ').split('+')[0], '%Y-%m-%d %H:%M:%S.%f') > datetime.datetime.today()):
                locationNames.append(locationMap[appts['entry'][i]['resource']['participant'][1]['actor']['reference'].split('/')[-1]])
                apptDate.append(appts['entry'][i]['resource']['start'].split('T')[0])

        return apptDate, locationNames

    def makeIndividualCSV(self):
        dates, names = self.getIndividualValues()
        count = [1] * len(dates)

        df = pd.DataFrame()
        df['date'] = dates
        df['community_name'] = names
        df['volume'] = count

        df = df.groupby(['date', 'community_name']).sum()

        df.to_csv('/Users/darinhunt/OnSpot/code/modmed/automated_email/files/file.csv')

    def getLocationZips(self):
        location_ids = []
        location_names = []

        x = getData('Location').getData()
        for i in range(len(x['entry'])):
            loc = x['entry'][i]['resource']['name']
            id = x['entry'][i]['resource']['id']
            location_ids.append(id)
            location_names.append(loc)

        return dict(zip(location_ids, location_names))
