# ServiceVOIPPresenceSetResetEditData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_presence_set_reset_edit_data import ServiceVOIPPresenceSetResetEditData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPPresenceSetResetEditData from a JSON string
service_voip_presence_set_reset_edit_data_instance = ServiceVOIPPresenceSetResetEditData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPPresenceSetResetEditData.to_json())

# convert the object into a dict
service_voip_presence_set_reset_edit_data_dict = service_voip_presence_set_reset_edit_data_instance.to_dict()
# create an instance of ServiceVOIPPresenceSetResetEditData from a dict
service_voip_presence_set_reset_edit_data_from_dict = ServiceVOIPPresenceSetResetEditData.from_dict(service_voip_presence_set_reset_edit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


