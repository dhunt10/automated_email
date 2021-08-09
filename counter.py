from first import getData
from resources import resources

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