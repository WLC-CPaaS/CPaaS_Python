# ServiceSystemStatusOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpaas_services** | [**ServiceSystemStatusCPAASService**](ServiceSystemStatusCPAASService.md) |  | [optional] 
**messaging_services** | [**ServiceSystemStatusMessagingService**](ServiceSystemStatusMessagingService.md) |  | [optional] 
**support_services** | [**ServiceSystemStatusSupportService**](ServiceSystemStatusSupportService.md) |  | [optional] 
**voip_services** | [**ServiceSystemStatusVOIPService**](ServiceSystemStatusVOIPService.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_system_status_output import ServiceSystemStatusOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSystemStatusOutput from a JSON string
service_system_status_output_instance = ServiceSystemStatusOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceSystemStatusOutput.to_json())

# convert the object into a dict
service_system_status_output_dict = service_system_status_output_instance.to_dict()
# create an instance of ServiceSystemStatusOutput from a dict
service_system_status_output_from_dict = ServiceSystemStatusOutput.from_dict(service_system_status_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


