# ServiceSystemStatusSupportService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e911_server** | **str** |  | [optional] 
**phone_number_server** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_system_status_support_service import ServiceSystemStatusSupportService

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSystemStatusSupportService from a JSON string
service_system_status_support_service_instance = ServiceSystemStatusSupportService.from_json(json)
# print the JSON string representation of the object
print(ServiceSystemStatusSupportService.to_json())

# convert the object into a dict
service_system_status_support_service_dict = service_system_status_support_service_instance.to_dict()
# create an instance of ServiceSystemStatusSupportService from a dict
service_system_status_support_service_from_dict = ServiceSystemStatusSupportService.from_dict(service_system_status_support_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


