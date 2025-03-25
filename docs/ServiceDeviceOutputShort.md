# ServiceDeviceOutputShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_recording** | [**ServiceCallRecordingSettings**](ServiceCallRecordingSettings.md) |  | [optional] 
**device_type** | **str** |  | [optional] 
**do_not_disturb** | [**ServiceVOIPSharedDoNotDisturb**](ServiceVOIPSharedDoNotDisturb.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_device_output_short import ServiceDeviceOutputShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeviceOutputShort from a JSON string
service_device_output_short_instance = ServiceDeviceOutputShort.from_json(json)
# print the JSON string representation of the object
print(ServiceDeviceOutputShort.to_json())

# convert the object into a dict
service_device_output_short_dict = service_device_output_short_instance.to_dict()
# create an instance of ServiceDeviceOutputShort from a dict
service_device_output_short_from_dict = ServiceDeviceOutputShort.from_dict(service_device_output_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


