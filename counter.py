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

    # add in a date range and add to yesterdays numbers
    # just pull fresh data for total patients, appointments and encounters and slots

    def totalPatients(self):
        """
        gets the total number of patients book over all time
        :return: total number of patients book all time
        """
        x = getData(self.resource.PATIENT.value, self.auth).getData()
        return x['total']

    def getNewPatients(self):
        """

        :return: returns the number of new patients in the last 24 hours
        """
        x = getData(self.resource.PATIENT.value, self.auth).getDailyData()
        return x['total']
    
    def totalAppointments(self):
        """

        :return: total number of appointments booked over all time
        """
        x = getData(self.resource.APPOINTMENT.value, self.auth).getData()
        return x['total']

    def getNewAppointments(self):
        """

        :return: the number of new appointments booked in the last 24 hours
        """
        x = getData(self.resource.APPOINTMENT.value, self.auth).getDailyData()
        print('here: {}'.format(x['total']))
        return x['total']

    def totalFutureAppointments(self):
        """

        :return: all appointments in the future
        """
        count = 0
        x = getData(self.resource.APPOINTMENT.value, self.auth).getData()
        for i in range(len(x['entry'])):
            if datetime.datetime.strptime(x['entry'][i]['resource']['start'].replace('T', ' ').split('+')[0] , '%Y-%m-%d %H:%M:%S.%f') > datetime.datetime.today():
                count = count + 1
        return count

    def getFutureAppointmentsDaily(self):
        x = getData(self.resource.APPOINTMENT.value, self.auth).getDailyData()
        return x['total']

    def totalLocations(self):
        """

        :return: all locations
        """
        x = getData(self.resource.LOCATION.value, self.auth).getData()
        return x['total']

    def totalEncounters(self):
        """

        :return: total encounters of all time
        """
        x = getData(self.resource.ENCOUNTER.value, self.auth).getData()
        return x['total']

    def getNewEncounters(self):
        """

        :return: number of encounters in the ast 24 hours
        """
        x = getData(self.resource.ENCOUNTER.value, self.auth).getDailyData()
        return x['total']

    def totalProviders(self):
        """

        :return: number of providers we have
        """
        x = getData(self.resource.PRACTITIONER.value, self.auth).getData()
        return x['total']

    def totalSlots(self):
        """

        :return: no being used
        """
        x = getData(self.resource.SLOT.value, self.auth).getData()
        return x['total']