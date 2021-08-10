from oldNumbers import getOldNumbers

class updateNumbers:
    def __init__(self):
        """

        """
        self.oldNumbers = getOldNumbers()

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
