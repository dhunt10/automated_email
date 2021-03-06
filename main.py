from auth import getToken
from counter import newNumbers
from updateNumbers import updateNumbers
from email_sender import sendEmail
from location_count import locationManager

if __name__ == "__main__":

	auth = getToken().getToken()
	update = newNumbers(auth)
	newValues = updateNumbers(auth)
	email = sendEmail('Volume Report', auth)
	encounters = update.totalEncounters()
	total_appointments = update.totalAppointments()
	total_locations = update.totalLocations()
	total_patients = update.totalPatients()
	total_providers = update.totalProviders()
	total_encounters = update.totalEncounters()
	future_appointments = update.totalFutureAppointments()
	derma_drives = locationManager(auth).getTotalDrivesHistory()

	new_appointments = newValues.updateAppointmentNumbers(total_appointments)
	new_patients = newValues.updatePatientNumbers(total_patients)
	new_providers = newValues.updateProviderNumbers(total_providers)
	new_locations = newValues.updateLocationNumbers(total_locations)
	newValues.updateEncounterNumbers(total_encounters)



