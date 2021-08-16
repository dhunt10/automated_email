from enum import Enum

class resources(Enum):
	PATIENT = 'Patient' #NEEDED
	COVERAGE = 'Coverage' #CHECK
	PRACTITIONER = 'Practitioner' #NEEDED
	LOCATION = 'Location' #NEEDED
	DOCUMENT_REFERENCE = 'DocumentReference'
	APPOINTMENT = 'Appointment' #NEEDED
	SLOT = 'Slot' #NEEDED
	MEDICATION_STATEMENT = 'MedicationStatement'
	ALLERGY_INTOLERANCE = 'AllergyIntolerance'
	CONDITION = 'Condition'
	FAMILY_MEMBER_HISTORY = 'FamilyMemberHistory'
	ENCOUNTER = 'Encounter' #NEEDED
	CHARGE_ITEM = 'ChargeItem'
	ACCOUNT = 'Account'
	RELATED_PERSON = 'RelatedPerson'
	SERVICE_REQUEST = 'ServiceRequest'
	DIAGNOSTIC_REPORT = 'DiagnosticReport'
	TASK = 'Task'
