from first import getData
from resources import resources
import datetime

class newNumbers():

    def __init__(self):
        """
        This class is responsible for getting the most up to date numbers
	    """
        self.resource = resources()

    def totalPatients(self):
        x = getData(self.resource.PATIENT).getData()
        return x['total']
    
    def totalAppointments(self):
        x = getData(self.resource.APPOINTMENT).getData()
        return x['total']

    def totalFutureAppointments(self):
        count = 0
        x = getData(self.resource.APPOINTMENT).getData()
        for i in range(len(x['entry'])):
            if datetime.datetime.strptime(x['entry'][i]['resource']['start'].replace('T', ' ').split('+')[0] , '%Y-%m-%d %H:%M:%S.%f') > datetime.datetime.today():
                count = count + 1
        return count

    def totalLocations(self):
        x = getData(self.resource.LOCATION).getData()
        return x['total']

    def totalEncounters(self):
        x = getData(self.resource.ENCOUNTER).getData()
        return x['total']

    def totalProviders(self):
        x = getData(self.resource.PRACTITIONER).getData()
        return x['total']

    def totalSlots(self):
        x = getData(self.resource.SLOT).getData()
        return x['total']