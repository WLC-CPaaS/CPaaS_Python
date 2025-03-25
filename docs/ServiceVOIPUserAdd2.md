# ServiceVOIPUserAdd2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_forward** | [**ServiceCallForward**](ServiceCallForward.md) |  | [optional] 
**call_recording** | [**ServiceCallRecordingSettings**](ServiceCallRecordingSettings.md) |  | [optional] 
**do_not_disturb** | [**ServiceVOIPSharedDoNotDisturb**](ServiceVOIPSharedDoNotDisturb.md) |  | [optional] 
**email** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**music_on_hold** | [**ServiceMusicOnHold**](ServiceMusicOnHold.md) |  | [optional] 
**presence_id** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_user_add2 import ServiceVOIPUserAdd2

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPUserAdd2 from a JSON string
service_voip_user_add2_instance = ServiceVOIPUserAdd2.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPUserAdd2.to_json())

# convert the object into a dict
service_voip_user_add2_dict = service_voip_user_add2_instance.to_dict()
# create an instance of ServiceVOIPUserAdd2 from a dict
service_voip_user_add2_from_dict = ServiceVOIPUserAdd2.from_dict(service_voip_user_add2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


