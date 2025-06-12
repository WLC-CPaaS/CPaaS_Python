# ModelsTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**firmware_id** | **str** |  | [optional] 
**firmware_version** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**model_name** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.models_template import ModelsTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsTemplate from a JSON string
models_template_instance = ModelsTemplate.from_json(json)
# print the JSON string representation of the object
print(ModelsTemplate.to_json())

# convert the object into a dict
models_template_dict = models_template_instance.to_dict()
# create an instance of ModelsTemplate from a dict
models_template_from_dict = ModelsTemplate.from_dict(models_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


