# ServiceVOIPAccountCallRecording


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**ServiceCallRecordingSettings**](ServiceCallRecordingSettings.md) |  | [optional] 
**endpoint** | [**ServiceCallRecordingSettings**](ServiceCallRecordingSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_account_call_recording import ServiceVOIPAccountCallRecording

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPAccountCallRecording from a JSON string
service_voip_account_call_recording_instance = ServiceVOIPAccountCallRecording.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPAccountCallRecording.to_json())

# convert the object into a dict
service_voip_account_call_recording_dict = service_voip_account_call_recording_instance.to_dict()
# create an instance of ServiceVOIPAccountCallRecording from a dict
service_voip_account_call_recording_from_dict = ServiceVOIPAccountCallRecording.from_dict(service_voip_account_call_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


