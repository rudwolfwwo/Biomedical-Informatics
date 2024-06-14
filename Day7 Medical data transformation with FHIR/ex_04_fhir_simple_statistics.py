from fhir.resources.patient import Patient
from fhir.resources.encounter import Encounter
from fhir.resources.organization import Organization
from ex_03_fhir import loadResources

from datetime import date, datetime
from dateutil.relativedelta import relativedelta

def getAge(birthday):
    today = date.today()
    return relativedelta(today, birthday).years

def computeAgeAverage(filter=True):
    list = loadResources("Patient",filter)
    if len(list) == 0:
        return -1
    ages = []
    for patient in list:
        ages.append(getAge(patient.birthDate))
    return sum(ages)/len(ages)



def computeDeceasedPercentage(filter=True):
    list = loadResources("Patient", filter)
    if len(list) == 0:
        return -1
    dead = 0
    for patient in list:
        if patient.deceasedBoolean == True or patient.deceasedDateTime != None:
            dead += 1
    return dead/len(list)
