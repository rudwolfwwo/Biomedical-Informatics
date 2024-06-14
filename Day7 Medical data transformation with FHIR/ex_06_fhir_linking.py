from fhir.resources.patient import Patient
from fhir.resources.encounter import Encounter
from fhir.resources.organization import Organization

from fhir.resources.address import Address
from fhir.resources.humanname import HumanName
from fhir.resources.period import Period
from fhir.resources.reference import Reference
from fhir.resources.coding import Coding
from datetime import date, datetime, timezone
from ex_03_fhir import loadResources, uploadResource
from ex_05_fhir_create_custom import createCustomPatient, createOrRetrievePatientOnServer, createCustomOrganization, createOrRetrieveOrganizationOnServer

def createCustomEncounter(pat_id, org_id):
    subject = Reference(reference="Patient/" + str(pat_id))
    serviceProvider = Reference(reference="Organization/" + str(org_id))
    status = "finished"
    return Encounter(serviceProvider=serviceProvider,subject=subject,status=status)

def lookupCustomEncounterOnServer(given_fhir_enc):
    list = loadResources("Encounter", False)
    for enc in list:
        if enc.serviceProvider == given_fhir_enc.serviceProvider and enc.subject == given_fhir_enc.subject:
            return enc
    return None

def createOrRetrieveEncounterOnServer(given_fhir_enc):
    enc = lookupCustomEncounterOnServer(given_fhir_enc)
    if enc is None:
        uploadResource(given_fhir_enc)
        enc = lookupCustomEncounterOnServer(given_fhir_enc)
    return enc

def linkAndCreateFHIRObjects():
    pat = createCustomPatient()
    pat_on_server = createOrRetrievePatientOnServer(pat)

    assert pat_on_server.id is not None

    org = createCustomOrganization()
    org_on_server = createOrRetrieveOrganizationOnServer(org)

    assert org_on_server.id is not None

    enc = createCustomEncounter(pat.id, org.id)
    enc_on_server = createOrRetrieveEncounterOnServer(enc)

    assert enc_on_server.id is not None

#linkAndCreateFHIRObjects()

