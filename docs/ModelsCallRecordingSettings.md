# ModelsCallRecordingSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any** | [**ModelsCallRecordingSource**](ModelsCallRecordingSource.md) |  | [optional] 
**inbound** | [**ModelsCallRecordingSource**](ModelsCallRecordingSource.md) |  | [optional] 
**outbound** | [**ModelsCallRecordingSource**](ModelsCallRecordingSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.models_call_recording_settings import ModelsCallRecordingSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsCallRecordingSettings from a JSON string
models_call_recording_settings_instance = ModelsCallRecordingSettings.from_json(json)
# print the JSON string representation of the object
print(ModelsCallRecordingSettings.to_json())

# convert the object into a dict
models_call_recording_settings_dict = models_call_recording_settings_instance.to_dict()
# create an instance of ModelsCallRecordingSettings from a dict
models_call_recording_settings_from_dict = ModelsCallRecordingSettings.from_dict(models_call_recording_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


