from oldNumbers import getOldNumbers
from counter import newNumbers

class updateNumbers:
    def __init__(self, auth=None):
        """

        """
        self.oldNumbers = getOldNumbers()
        self.newNumbers = newNumbers(auth)

    def updateLocationNumbers(self, number):
        old = self.oldNumbers.getLocationNumbers()
        new = number
        diff = new - old
        self.oldNumbers.updateLocationNumbers(new)
        return diff

    def updatePatientNumbers(self, number):
        old = self.oldNumbers.getPatientNumbers()
        new = number
        diff = new - old
        self.oldNumbers.updatePatientNumbers(new)
        return diff

    def updateProviderNumbers(self, number):
        old = self.oldNumbers.getProviderNumbers()
        new = number
        diff = new - old
        self.oldNumbers.updateProviderNumbers(new)
        return diff

    def updateEncounterNumbers(self, number):
        self.oldNumbers.updateEncounterNumbers(number)

    def updateAppointmentNumbers(self, number):
        old = self.oldNumbers.getAppointmentNumbers()
        new = number
        diff = new - old
        self.oldNumbers.updateAppointmentNumbers(new)
        return diff


    def updatePatientDaily(self):
        old = self.oldNumbers.getPatientNumbers()
        value = self.newNumbers.getNewPatients()
        new = value + old
        self.oldNumbers.updatePatientNumbers(new)
        return new, value

    def updateEncounterDaily(self):
        old = self.oldNumbers.getEncounterNumbers()
        value = self.newNumbers.getNewEncounters()
        new = value + old
        self.oldNumbers.updateEncounterNumbers(new)
        return new, value

    def updateAppointmentDaily(self):
        old = self.oldNumbers.getAppointmentNumbers()
        value = self.newNumbers.getNewAppointments()
        new = value + old
        self.oldNumbers.updateAppointmentNumbers(new)
        return new, value

    def updateFutureAppointmentsDaily(self):
        old = self.oldNumbers.getFutureAppointmentDailyNumbers()
        value = self.newNumbers.getFutureAppointmentsDaily()
        new = value + old
        self.oldNumbers.updateFutureAppointmentDailyNumbers()
        return new, value