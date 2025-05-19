# ModelsUserOutputFullCallerid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emergency** | [**ModelsUserOutputFullCalleridEmergency**](ModelsUserOutputFullCalleridEmergency.md) |  | [optional] 
**external** | [**ModelsUserOutputFullCalleridExternal**](ModelsUserOutputFullCalleridExternal.md) |  | [optional] 
**internal** | [**ModelsUserOutputFullCalleridInternal**](ModelsUserOutputFullCalleridInternal.md) |  | [optional] 

## Example

```python
from openapi_client.models.models_user_output_full_callerid import ModelsUserOutputFullCallerid

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsUserOutputFullCallerid from a JSON string
models_user_output_full_callerid_instance = ModelsUserOutputFullCallerid.from_json(json)
# print the JSON string representation of the object
print(ModelsUserOutputFullCallerid.to_json())

# convert the object into a dict
models_user_output_full_callerid_dict = models_user_output_full_callerid_instance.to_dict()
# create an instance of ModelsUserOutputFullCallerid from a dict
models_user_output_full_callerid_from_dict = ModelsUserOutputFullCallerid.from_dict(models_user_output_full_callerid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


