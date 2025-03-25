# ServiceSystemStatusCPAASService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend** | **str** |  | [optional] 
**portal** | **str** |  | [optional] 
**server** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_system_status_cpaas_service import ServiceSystemStatusCPAASService

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSystemStatusCPAASService from a JSON string
service_system_status_cpaas_service_instance = ServiceSystemStatusCPAASService.from_json(json)
# print the JSON string representation of the object
print(ServiceSystemStatusCPAASService.to_json())

# convert the object into a dict
service_system_status_cpaas_service_dict = service_system_status_cpaas_service_instance.to_dict()
# create an instance of ServiceSystemStatusCPAASService from a dict
service_system_status_cpaas_service_from_dict = ServiceSystemStatusCPAASService.from_dict(service_system_status_cpaas_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


