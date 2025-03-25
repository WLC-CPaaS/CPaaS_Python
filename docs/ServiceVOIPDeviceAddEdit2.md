# ServiceVOIPDeviceAddEdit2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_forward** | [**ServiceCallForward**](ServiceCallForward.md) |  | [optional] 
**call_recording** | [**ServiceCallRecordingSettings**](ServiceCallRecordingSettings.md) |  | [optional] 
**caller_id** | [**ServiceVOIPDeviceAddEdit3c**](ServiceVOIPDeviceAddEdit3c.md) |  | [optional] 
**device_type** | **str** |  | [optional] 
**do_not_disturb** | [**ServiceVOIPSharedDoNotDisturb**](ServiceVOIPSharedDoNotDisturb.md) |  | [optional] 
**enabled** | **bool** | cannot use required, else it has to be true and false is not allowed | [optional] 
**mac_address** | **str** | dont use mac, it enforces :, which voip does not like | [optional] 
**music_on_hold** | [**ServiceMusicOnHold**](ServiceMusicOnHold.md) |  | [optional] 
**name** | **str** |  | 
**owner_id** | **str** | json omitempty is needed else voip fails on \&quot;\&quot; for owner_id | [optional] 
**sip** | [**ServiceVOIPDeviceAddEdit3a**](ServiceVOIPDeviceAddEdit3a.md) |  | 

## Example

```python
from openapi_client.models.service_voip_device_add_edit2 import ServiceVOIPDeviceAddEdit2

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPDeviceAddEdit2 from a JSON string
service_voip_device_add_edit2_instance = ServiceVOIPDeviceAddEdit2.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPDeviceAddEdit2.to_json())

# convert the object into a dict
service_voip_device_add_edit2_dict = service_voip_device_add_edit2_instance.to_dict()
# create an instance of ServiceVOIPDeviceAddEdit2 from a dict
service_voip_device_add_edit2_from_dict = ServiceVOIPDeviceAddEdit2.from_dict(service_voip_device_add_edit2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


