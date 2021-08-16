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
    total_encounters, new_encounters = newValues.updateEncounterDaily()
    total_patients, new_patients = newValues.updatePatientDaily()
    total_appointments, new_appointments = newValues.updateAppointmentDaily()
    total_locations = update.totalLocations()
    total_providers = update.totalProviders()
    future_appointments = update.getFutureAppointmentsDaily()
    derma_drives = locationManager(auth).getTotalDrivesHistory()

    new_providers = newValues.updateProviderNumbers(total_providers)
    new_locations = newValues.updateLocationNumbers(total_locations)

    email.prepare_email(total_locations, total_patients, total_providers,
                        total_encounters, total_appointments, new_appointments,
                        new_patients, future_appointments, derma_drives)