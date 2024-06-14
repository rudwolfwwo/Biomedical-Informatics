from ex_03_fhir import loadResources, deleteResource

def deleteResources():
    for res in loadResources(resource_type="Patient",filter=True):
        deleteResource(res)
    for res in loadResources(resource_type="Organization", filter=True):
        deleteResource(res)
    for res in loadResources(resource_type="Encounter", filter=True):
        deleteResource(res)
