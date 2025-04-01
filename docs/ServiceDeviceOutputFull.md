# ServiceDeviceOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_forward** | [**ServiceCallForward**](ServiceCallForward.md) |  | [optional] 
**call_recording** | [**ServiceCallRecordingSettings**](ServiceCallRecordingSettings.md) |  | [optional] 
**caller_id** | [**ServiceDeviceOutputFullCallerid**](ServiceDeviceOutputFullCallerid.md) |  | [optional] 
**device_type** | **str** |  | [optional] 
**do_not_disturb** | [**ServiceVOIPSharedDoNotDisturb**](ServiceVOIPSharedDoNotDisturb.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**media** | [**ServiceDeviceOutputFullMedia**](ServiceDeviceOutputFullMedia.md) |  | [optional] 
**music_on_hold** | [**ServiceMusicOnHold**](ServiceMusicOnHold.md) | Provision  *DeviceOutputFullProvision &#x60;json:\&quot;provision\&quot;&#x60; | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**sip** | [**ServiceDeviceOutputFullSIP**](ServiceDeviceOutputFullSIP.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_device_output_full import ServiceDeviceOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeviceOutputFull from a JSON string
service_device_output_full_instance = ServiceDeviceOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceDeviceOutputFull.to_json())

# convert the object into a dict
service_device_output_full_dict = service_device_output_full_instance.to_dict()
# create an instance of ServiceDeviceOutputFull from a dict
service_device_output_full_from_dict = ServiceDeviceOutputFull.from_dict(service_device_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


