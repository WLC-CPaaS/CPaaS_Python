# ServiceUserOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_forward** | [**ServiceCallForward**](ServiceCallForward.md) |  | [optional] 
**call_recording** | [**ServiceCallRecordingSettings**](ServiceCallRecordingSettings.md) |  | [optional] 
**do_not_disturb** | [**ServiceVOIPSharedDoNotDisturb**](ServiceVOIPSharedDoNotDisturb.md) |  | [optional] 
**email** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**music_on_hold** | [**ServiceMusicOnHold**](ServiceMusicOnHold.md) |  | [optional] 
**presence_id** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.service_user_output_full import ServiceUserOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUserOutputFull from a JSON string
service_user_output_full_instance = ServiceUserOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceUserOutputFull.to_json())

# convert the object into a dict
service_user_output_full_dict = service_user_output_full_instance.to_dict()
# create an instance of ServiceUserOutputFull from a dict
service_user_output_full_from_dict = ServiceUserOutputFull.from_dict(service_user_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


