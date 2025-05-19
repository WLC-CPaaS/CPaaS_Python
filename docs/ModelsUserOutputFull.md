# ModelsUserOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_forward** | [**ModelsCallForward**](ModelsCallForward.md) |  | [optional] 
**call_recording** | [**ModelsCallRecordingSettings**](ModelsCallRecordingSettings.md) |  | [optional] 
**caller_id** | [**ModelsUserOutputFullCallerid**](ModelsUserOutputFullCallerid.md) |  | [optional] 
**do_not_disturb** | [**ModelsVOIPSharedDoNotDisturb**](ModelsVOIPSharedDoNotDisturb.md) |  | [optional] 
**email** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**music_on_hold** | [**ModelsMusicOnHold**](ModelsMusicOnHold.md) |  | [optional] 
**presence_id** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.models_user_output_full import ModelsUserOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsUserOutputFull from a JSON string
models_user_output_full_instance = ModelsUserOutputFull.from_json(json)
# print the JSON string representation of the object
print(ModelsUserOutputFull.to_json())

# convert the object into a dict
models_user_output_full_dict = models_user_output_full_instance.to_dict()
# create an instance of ModelsUserOutputFull from a dict
models_user_output_full_from_dict = ModelsUserOutputFull.from_dict(models_user_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


