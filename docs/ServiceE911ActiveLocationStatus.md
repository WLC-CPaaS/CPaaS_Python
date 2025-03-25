# ServiceE911ActiveLocationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_e911_active_location_status import ServiceE911ActiveLocationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911ActiveLocationStatus from a JSON string
service_e911_active_location_status_instance = ServiceE911ActiveLocationStatus.from_json(json)
# print the JSON string representation of the object
print(ServiceE911ActiveLocationStatus.to_json())

# convert the object into a dict
service_e911_active_location_status_dict = service_e911_active_location_status_instance.to_dict()
# create an instance of ServiceE911ActiveLocationStatus from a dict
service_e911_active_location_status_from_dict = ServiceE911ActiveLocationStatus.from_dict(service_e911_active_location_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


