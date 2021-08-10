import mysql.connector

class getOldNumbers:

  def __init__(self):
    self.mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Familyguy10",
    database="onspot_patient_count",
    auth_plugin='mysql_native_password'
  )


#todo location differences are not calculated on an individual basis for location because we do not save them into mysql
  def getLocationNumbers(self):
      mycursor = self.mydb.cursor()
      mycursor.execute('select location_total from location_count where count_id = 1')
      return mycursor.fetchall()[0][0]

  def getPatientNumbers(self):
      mycursor = self.mydb.cursor()
      mycursor.execute('select patient_total from patient_count where count_id = 1;')
      return mycursor.fetchall()[0][0]

  def getProviderNumbers(self):
      mycursor = self.mydb.cursor()
      mycursor.execute('select provider_total from provider_count where count_id = 1;')
      return mycursor.fetchall()[0][0]

  def getEncounterNumbers(self):
      mycursor = self.mydb.cursor()
      mycursor.execute('select encounter_total from encounter_count where count_id = 1;')
      return mycursor.fetchall()[0][0]

  def getAppointmentNumbers(self):
      mycursor = self.mydb.cursor()
      mycursor.execute('select appointment_total from appointment_count where count_id = 1;')
      return mycursor.fetchall()[0][0]

  def updateLocationNumbers(self, new_value):
      mycursor = self.mydb.cursor()
      mycursor.execute('update location_count set location_total = {} where count_id = 1;'.format(new_value))
      self.mydb.commit()

  def updatePatientNumbers(self, new_value):
      mycursor = self.mydb.cursor()
      mycursor.execute('update patient_count set patient_total = {} where count_id = 1;'.format(new_value))
      self.mydb.commit()

  def updateProviderNumbers(self, new_value):
      mycursor = self.mydb.cursor()
      mycursor.execute('update provider_count set provider_total = {} where count_id = 1;'.format(new_value))
      self.mydb.commit()

  def updateEncounterNumbers(self, new_value):
      mycursor = self.mydb.cursor()
      mycursor.execute('update encounter_count set encounter_total = {} where count_id = 1;'.format(new_value))
      self.mydb.commit()

  def updateAppointmentNumbers(self, new_value):
      mycursor = self.mydb.cursor()
      mycursor.execute('update appointment_count set appointment_total = {} where count_id = 1;'.format(new_value))
      self.mydb.commit()



