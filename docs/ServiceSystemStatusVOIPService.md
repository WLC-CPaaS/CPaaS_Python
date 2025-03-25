# ServiceSystemStatusVOIPService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | **str** |  | [optional] 
**backend** | **str** |  | [optional] 
**call_manager** | **str** |  | [optional] 
**media_server** | **str** |  | [optional] 
**message_broker** | **str** |  | [optional] 
**sip_proxy** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_system_status_voip_service import ServiceSystemStatusVOIPService

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSystemStatusVOIPService from a JSON string
service_system_status_voip_service_instance = ServiceSystemStatusVOIPService.from_json(json)
# print the JSON string representation of the object
print(ServiceSystemStatusVOIPService.to_json())

# convert the object into a dict
service_system_status_voip_service_dict = service_system_status_voip_service_instance.to_dict()
# create an instance of ServiceSystemStatusVOIPService from a dict
service_system_status_voip_service_from_dict = ServiceSystemStatusVOIPService.from_dict(service_system_status_voip_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


