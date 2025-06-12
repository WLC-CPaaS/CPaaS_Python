# ModelsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**model_name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.models_model import ModelsModel

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsModel from a JSON string
models_model_instance = ModelsModel.from_json(json)
# print the JSON string representation of the object
print(ModelsModel.to_json())

# convert the object into a dict
models_model_dict = models_model_instance.to_dict()
# create an instance of ModelsModel from a dict
models_model_from_dict = ModelsModel.from_dict(models_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


