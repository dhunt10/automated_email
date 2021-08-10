import json
from first import getData
from resources import resources
from counter import newNumbers
from updateNumbers import updateNumbers
from email_sender import sendEmail
from location_count import locationManager

if __name__ == "__main__":
	update = newNumbers()
	newValues = updateNumbers()
	email = sendEmail('Volume Report')
	encounters = update.totalEncounters()
	total_appointments = update.totalAppointments()
	total_locations = update.totalLocations()
	total_patients = update.totalPatients()
	total_providers = update.totalProviders()
	total_encounters = update.totalEncounters()
	available_slots = update.totalSlots()
	future_appointments = update.totalFutureAppointments()
	derma_drives = locationManager().getTotalDrivesHistory()

	new_appointments = newValues.updateAppointmentNumbers(total_appointments)
	new_patients = newValues.updatePatientNumbers(total_patients)
	new_providers = newValues.updateProviderNumbers(total_providers)
	new_locations = newValues.updateLocationNumbers(total_locations)
	newValues.updateEncounterNumbers(total_encounters)
	email.prepare_email(total_locations, total_patients, total_providers,
						total_encounters, total_appointments, new_appointments,
						new_patients, available_slots, future_appointments, derma_drives)



