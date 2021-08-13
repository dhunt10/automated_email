from first import getData
from resources import resources
import datetime

class newNumbers():

    def __init__(self, auth):
        """
        This class is responsible for getting the most up to date numbers
	    """
        self.resource = resources
        self.auth = auth

    def totalPatients(self):
        x = getData(self.resource.PATIENT.value, self.auth).getData()
        return x['total']
    
    def totalAppointments(self):
        x = getData(self.resource.APPOINTMENT.value, self.auth).getData()
        return x['total']

    def totalFutureAppointments(self):
        count = 0
        x = getData(self.resource.APPOINTMENT.value, self.auth).getData()
        for i in range(len(x['entry'])):
            if datetime.datetime.strptime(x['entry'][i]['resource']['start'].replace('T', ' ').split('+')[0] , '%Y-%m-%d %H:%M:%S.%f') > datetime.datetime.today():
                count = count + 1
        return count

    def totalLocations(self):
        x = getData(self.resource.LOCATION.value, self.auth).getData()
        return x['total']

    def totalEncounters(self):
        x = getData(self.resource.ENCOUNTER.value, self.auth).getData()
        return x['total']

    def totalProviders(self):
        x = getData(self.resource.PRACTITIONER.value, self.auth).getData()
        return x['total']

    def totalSlots(self):
        x = getData(self.resource.SLOT.value, self.auth).getData()
        return x['total']