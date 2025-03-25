# ServiceCallRecordingSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any** | [**ServiceCallRecordingSource**](ServiceCallRecordingSource.md) |  | [optional] 
**inbound** | [**ServiceCallRecordingSource**](ServiceCallRecordingSource.md) |  | [optional] 
**outbound** | [**ServiceCallRecordingSource**](ServiceCallRecordingSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_call_recording_settings import ServiceCallRecordingSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallRecordingSettings from a JSON string
service_call_recording_settings_instance = ServiceCallRecordingSettings.from_json(json)
# print the JSON string representation of the object
print(ServiceCallRecordingSettings.to_json())

# convert the object into a dict
service_call_recording_settings_dict = service_call_recording_settings_instance.to_dict()
# create an instance of ServiceCallRecordingSettings from a dict
service_call_recording_settings_from_dict = ServiceCallRecordingSettings.from_dict(service_call_recording_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


