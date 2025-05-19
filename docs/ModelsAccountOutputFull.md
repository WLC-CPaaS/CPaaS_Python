# ModelsAccountOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_id** | [**ModelsVOIPAccountOutputFullCallerid**](ModelsVOIPAccountOutputFullCallerid.md) |  | [optional] 
**do_not_disturb** | [**ModelsVOIPSharedDoNotDisturb**](ModelsVOIPSharedDoNotDisturb.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**music_on_hold** | [**ModelsVOIPAccountMusicOnHold**](ModelsVOIPAccountMusicOnHold.md) |  | [optional] 
**name** | **str** |  | [optional] 
**realm** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.models_account_output_full import ModelsAccountOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsAccountOutputFull from a JSON string
models_account_output_full_instance = ModelsAccountOutputFull.from_json(json)
# print the JSON string representation of the object
print(ModelsAccountOutputFull.to_json())

# convert the object into a dict
models_account_output_full_dict = models_account_output_full_instance.to_dict()
# create an instance of ModelsAccountOutputFull from a dict
models_account_output_full_from_dict = ModelsAccountOutputFull.from_dict(models_account_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


