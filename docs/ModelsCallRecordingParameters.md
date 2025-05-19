# ModelsCallRecordingParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**format** | **str** |  | [optional] 
**record_min_sec** | **int** |  | [optional] 
**record_on_answer** | **bool** |  | [optional] 
**record_on_bridge** | **bool** |  | [optional] 
**record_sample_rate** | **int** |  | [optional] 
**time_limit** | **int** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.models_call_recording_parameters import ModelsCallRecordingParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsCallRecordingParameters from a JSON string
models_call_recording_parameters_instance = ModelsCallRecordingParameters.from_json(json)
# print the JSON string representation of the object
print(ModelsCallRecordingParameters.to_json())

# convert the object into a dict
models_call_recording_parameters_dict = models_call_recording_parameters_instance.to_dict()
# create an instance of ModelsCallRecordingParameters from a dict
models_call_recording_parameters_from_dict = ModelsCallRecordingParameters.from_dict(models_call_recording_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


