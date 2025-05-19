# ModelsCallRecordingSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any** | [**ModelsCallRecordingParameters**](ModelsCallRecordingParameters.md) |  | [optional] 
**offnet** | [**ModelsCallRecordingParameters**](ModelsCallRecordingParameters.md) |  | [optional] 
**onnet** | [**ModelsCallRecordingParameters**](ModelsCallRecordingParameters.md) |  | [optional] 

## Example

```python
from openapi_client.models.models_call_recording_source import ModelsCallRecordingSource

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsCallRecordingSource from a JSON string
models_call_recording_source_instance = ModelsCallRecordingSource.from_json(json)
# print the JSON string representation of the object
print(ModelsCallRecordingSource.to_json())

# convert the object into a dict
models_call_recording_source_dict = models_call_recording_source_instance.to_dict()
# create an instance of ModelsCallRecordingSource from a dict
models_call_recording_source_from_dict = ModelsCallRecordingSource.from_dict(models_call_recording_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


