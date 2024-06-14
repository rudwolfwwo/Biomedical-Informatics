from Day7.ex_00_settings import FHIR_API_ENDPOINT, RZ_KENNUNG
from fhir.resources.patient import Patient
from fhir.resources.encounter import Encounter
from fhir.resources.organization import Organization
from fhir.resources.identifier import Identifier
from ex_01_http import sendGETRequest, sendPOSTRequest, sendDELETERequest
import json, time

def uploadResource(resource):
    if resource.resource_type not in ["Patient","Encounter","Organization"]:
        raise Exception

    # KEEP THIS CODE SECTION
    if resource.identifier is None:
        resource.identifier = [Identifier(system="submitter", value=RZ_KENNUNG)]
    else:
        new_identifiers = [ entry for entry in resource.identifier if entry.system != "submitter"]
        new_identifiers.append(Identifier(system="submitter", value=RZ_KENNUNG))
        resource.identifier =new_identifiers
    # END OF KEEP THIS CODE SECTION

    x = sendPOSTRequest(FHIR_API_ENDPOINT + "/" + resource.resource_type + "?identifier=submitter|" + RZ_KENNUNG, resource.json())
    # Wait after upload to avoid server timing issues in test script
    time.sleep(2)
    if x[1] != 201:
        raise Exception
    return x[0]




def loadResources(resource_type, filter=False):
    add = "/" + resource_type
    if filter is True:
        add += "?identifier=submitter|" + RZ_KENNUNG
    t = sendGETRequest(FHIR_API_ENDPOINT + add)
    x = json.loads(t[0])
    if t[1] != 200:
        raise Exception

    res_list = []
    while True:
        if len(x["link"]) == 1:
            break
        for entry in x["entry"]:
            if entry["resource"]["resourceType"] not in ["Patient","Encounter","Organization"]:
                raise Exception
            elif entry["resource"]["resourceType"] == resource_type:
                if resource_type == "Patient":
                    res_list.append(Patient.parse_obj(entry["resource"]))
                elif resource_type == "Encounter":
                    res_list.append(Encounter.parse_obj(entry["resource"]))
                elif resource_type == "Organization":
                    res_list.append(Organization.parse_obj(entry["resource"]))

        url_to_call = ""
        for links in x.get("link",[]):
            if links["relation"] == "next": #len(x["link"]) == 2 and len(list) > 20:
                url_to_call = links["url"]
        if url_to_call == "":
            break
        x = json.loads(sendGETRequest(url_to_call)[0])
    return res_list

def deleteResource(resource):
    if resource.resource_type not in ["Patient","Encounter","Organization"]:
        raise Exception
    x = sendDELETERequest(FHIR_API_ENDPOINT + "/" + resource.resource_type + "?identifier=submitter|" + RZ_KENNUNG)
    time.sleep(2)
    if x[1] != 200:
        raise Exception
    return x[0]


