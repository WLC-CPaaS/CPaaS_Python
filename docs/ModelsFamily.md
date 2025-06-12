# ModelsFamily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**timezone_format_id** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.models_family import ModelsFamily

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsFamily from a JSON string
models_family_instance = ModelsFamily.from_json(json)
# print the JSON string representation of the object
print(ModelsFamily.to_json())

# convert the object into a dict
models_family_dict = models_family_instance.to_dict()
# create an instance of ModelsFamily from a dict
models_family_from_dict = ModelsFamily.from_dict(models_family_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


