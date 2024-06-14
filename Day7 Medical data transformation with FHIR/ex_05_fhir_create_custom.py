from fhir.resources.patient import Patient
from fhir.resources.encounter import Encounter
from fhir.resources.organization import Organization

from fhir.resources.address import Address
from fhir.resources.humanname import HumanName
from datetime import date
from ex_03_fhir import loadResources, uploadResource

def createCustomPatient():
    patient = Patient()
    patient.name = [
          HumanName(**{
            "family": "Meyer",
            "given": [
              "Maximilian"
            ]
          })
        ]
    patient.address = [
        {
            "line": [
              "Salomon-Idler-Straße 4"
            ],
            "city": "Augsburg",
            "state": "Bayern",
            "postalCode": "86159",
            "country": "Deutschland"
          }
        ]
    patient.birthDate = date(year=2000,month=1,day=1)
    patient.deceasedBoolean = False
    patient.gender = "male"
    return patient

def createCustomOrganization():
    organisation = Organization()
    organisation.name = "Universitätsklinikum Augsburg"
    return organisation


def lookupCustomOrganizationOnServer(given_fhir_org):
    orgs = loadResources("Organization", False)
    print(orgs)
    for org in orgs:
        if org.name == given_fhir_org.name:
            return org
    return None


def lookupCustomPatientOnServer(given_fhir_pat):
    patients = loadResources("Patient", False)
    for patient in patients:
        if patient.name == given_fhir_pat.name and patient.birthDate == given_fhir_pat.birthDate:
            return patient
    return None


def createOrRetrievePatientOnServer(given_fhir_pat):
    pat = lookupCustomPatientOnServer(given_fhir_pat)
    if pat is None:
        uploadResource(given_fhir_pat)
        pat = lookupCustomPatientOnServer(given_fhir_pat)
    return pat


def createOrRetrieveOrganizationOnServer(given_fhir_org):
    pat = lookupCustomOrganizationOnServer(given_fhir_org)
    if pat is None:
        uploadResource(given_fhir_org)
        pat = lookupCustomOrganizationOnServer(given_fhir_org)
    return pat

