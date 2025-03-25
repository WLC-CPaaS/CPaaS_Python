# ServiceUserOutputShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_recording** | [**ServiceCallRecordingSettings**](ServiceCallRecordingSettings.md) |  | [optional] 
**do_not_disturb** | [**ServiceVOIPSharedDoNotDisturb**](ServiceVOIPSharedDoNotDisturb.md) |  | [optional] 
**email** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**first_name** | **str** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**presence_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_user_output_short import ServiceUserOutputShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUserOutputShort from a JSON string
service_user_output_short_instance = ServiceUserOutputShort.from_json(json)
# print the JSON string representation of the object
print(ServiceUserOutputShort.to_json())

# convert the object into a dict
service_user_output_short_dict = service_user_output_short_instance.to_dict()
# create an instance of ServiceUserOutputShort from a dict
service_user_output_short_from_dict = ServiceUserOutputShort.from_dict(service_user_output_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


