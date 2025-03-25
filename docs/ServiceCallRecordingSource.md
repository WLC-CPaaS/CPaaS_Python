# ServiceCallRecordingSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any** | [**ServiceCallRecordingParameters**](ServiceCallRecordingParameters.md) |  | [optional] 
**offnet** | [**ServiceCallRecordingParameters**](ServiceCallRecordingParameters.md) |  | [optional] 
**onnet** | [**ServiceCallRecordingParameters**](ServiceCallRecordingParameters.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_call_recording_source import ServiceCallRecordingSource

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallRecordingSource from a JSON string
service_call_recording_source_instance = ServiceCallRecordingSource.from_json(json)
# print the JSON string representation of the object
print(ServiceCallRecordingSource.to_json())

# convert the object into a dict
service_call_recording_source_dict = service_call_recording_source_instance.to_dict()
# create an instance of ServiceCallRecordingSource from a dict
service_call_recording_source_from_dict = ServiceCallRecordingSource.from_dict(service_call_recording_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


