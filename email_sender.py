import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from location_count import locationManager
from email.mime.base import MIMEBase
from email import encoders
import tqdm
import os
from counter import *

class sendEmail:
    def __init__(self, subject, filename=None):
        self.subject = subject
        self.lm = locationManager()
        self.lm.makeIndividualCSV()
        #self.filename = '/Users/darinhunt/OnSpot/code/modmed/automated_email/files/file.csv'
        self.sender_email = 'dhunt10@gmail.com'
        self.password = 'Familyguy10!'
        """if we want to attached a file like a csv"""
        #self.p = MIMEBase('application', 'octet-stream')
        #self.filename = self.filename
        #self.attachment = open(filename, "rb")
        #self.p.set_payload((self.attachment).read())
        #encoders.encode_base64(self.p)
        #self.p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        self.s = smtplib.SMTP('smtp.gmail.com', 587)
        self.s.starttls()
        self.s.login(self.sender_email, self.password)

    def prepare_email(self, location, patient, provider, encounter,
                      appointment, appointment_diff, patient_diff,
                      available_slots, future_appointments):
        """
        :param data:
        :return:
        """
        self.email_message = self.generateMessage(location, patient, provider, encounter,
                                                  appointment, appointment_diff,
                                                  patient_diff, available_slots, future_appointments)
        self.sendEmail('darin@onspotdermatology.com')
        self.s.quit()

    def sendEmail(self, email):
        msg = MIMEMultipart()
        message = self.email_message
        msg['From'] = self.sender_email
        msg['To'] = email
        msg['Subject'] = self.subject
        msg.attach(MIMEText(message, 'plain'))
        #msg.attach(self.p)
        text = msg.as_string()
        self.s.sendmail(self.sender_email, email, text)

    def generateMessage(self, location, patient, provider, encounter,
                        appointment, appointment_diff, patient_diff,
                        available_slots, future_appointments):


        return "Here are the updated totals from yesterday: \n " \
               "Total Appointments booked: {} \n" \
               "Total Patients: {} \n" \
               "Total Locations: {} \n" \
               "Total Providers: {} \n" \
               "Total Encounters: {} \n\n\n" \
               "Yesterday we booked {} new appointments \n" \
               "Yesterday we made {} new patients \n" \
               "We currently have {} available appointments\n" \
               "Appointments in the future {}: \n\n\n" \
               "Attached is the report for individual communities".format(appointment, patient, location, provider,
                                                                encounter, appointment_diff,
                                                          patient_diff, available_slots, future_appointments)
