from fhir.resources.patient import Patient
from ex_01_http import sendGETRequest
from Day7.ex_00_settings import FHIR_API_ENDPOINT
import json

def demo_patient_id():
    x = sendGETRequest(FHIR_API_ENDPOINT + "/Patient/1")
    print(json.loads(x[0])["name"][0]["family"])
    return json.loads(x[0])["name"][0]["family"]

def demo_count_patients():
    x = sendGETRequest(FHIR_API_ENDPOINT + "/Patient?_total=accurate")
    print(json.loads(x[0])["total"])
    return json.loads(x[0])["total"]

def demo_fhir_patient():
    x = sendGETRequest(FHIR_API_ENDPOINT + "/Patient/1")
    print(Patient.parse_obj(json.loads(x[0])))
    return Patient.parse_obj(json.loads(x[0]))

