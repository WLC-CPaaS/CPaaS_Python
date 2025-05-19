# ModelsDeviceOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_forward** | [**ModelsCallForward**](ModelsCallForward.md) |  | [optional] 
**call_recording** | [**ModelsCallRecordingSettings**](ModelsCallRecordingSettings.md) |  | [optional] 
**caller_id** | [**ModelsDeviceOutputFullCallerid**](ModelsDeviceOutputFullCallerid.md) |  | [optional] 
**device_type** | **str** |  | [optional] 
**do_not_disturb** | [**ModelsVOIPSharedDoNotDisturb**](ModelsVOIPSharedDoNotDisturb.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**media** | [**ModelsDeviceOutputFullMedia**](ModelsDeviceOutputFullMedia.md) |  | [optional] 
**music_on_hold** | [**ModelsMusicOnHold**](ModelsMusicOnHold.md) |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**provision** | [**ModelsDeviceOutputFullProvision**](ModelsDeviceOutputFullProvision.md) |  | [optional] 
**sip** | [**ModelsDeviceOutputFullSIP**](ModelsDeviceOutputFullSIP.md) |  | [optional] 

## Example

```python
from openapi_client.models.models_device_output_full import ModelsDeviceOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsDeviceOutputFull from a JSON string
models_device_output_full_instance = ModelsDeviceOutputFull.from_json(json)
# print the JSON string representation of the object
print(ModelsDeviceOutputFull.to_json())

# convert the object into a dict
models_device_output_full_dict = models_device_output_full_instance.to_dict()
# create an instance of ModelsDeviceOutputFull from a dict
models_device_output_full_from_dict = ModelsDeviceOutputFull.from_dict(models_device_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


