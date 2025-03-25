# ServiceE911RemoveLocationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_e911_remove_location_status import ServiceE911RemoveLocationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911RemoveLocationStatus from a JSON string
service_e911_remove_location_status_instance = ServiceE911RemoveLocationStatus.from_json(json)
# print the JSON string representation of the object
print(ServiceE911RemoveLocationStatus.to_json())

# convert the object into a dict
service_e911_remove_location_status_dict = service_e911_remove_location_status_instance.to_dict()
# create an instance of ServiceE911RemoveLocationStatus from a dict
service_e911_remove_location_status_from_dict = ServiceE911RemoveLocationStatus.from_dict(service_e911_remove_location_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


