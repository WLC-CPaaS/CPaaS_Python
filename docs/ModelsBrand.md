# ModelsBrand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.models_brand import ModelsBrand

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsBrand from a JSON string
models_brand_instance = ModelsBrand.from_json(json)
# print the JSON string representation of the object
print(ModelsBrand.to_json())

# convert the object into a dict
models_brand_dict = models_brand_instance.to_dict()
# create an instance of ModelsBrand from a dict
models_brand_from_dict = ModelsBrand.from_dict(models_brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


