FHIR_API_ENDPOINT = "http://137.250.168.21:8090/hapi-fhir-jpaserver/fhir"
HTTP_TEST_ENDPOINT = "http://137.250.168.21:8089"
RZ_KENNUNG  = "graanja"

# Internal checks & methods
import re
assert re.match(r"[a-z]{7,8}.?", RZ_KENNUNG) is not None

def test_updateFHIREndpoint(endpoint):
    global FHIR_API_ENDPOINT
    FHIR_API_ENDPOINT = endpoint

def test_updateHTTPEndpoint(endpoint):
    global HTTP_TEST_ENDPOINT
    HTTP_TEST_ENDPOINT = endpoint

def test_updateRZKennung(rz):
    global RZ_KENNUNG
    RZ_KENNUNG = rz