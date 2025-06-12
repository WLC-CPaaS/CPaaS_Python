# ModelsGenerateConfigFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**ModelsConfigFileParameter**](ModelsConfigFileParameter.md) |  | 
**template_file_id** | **str** |  | 
**template_id** | **str** |  | 

## Example

```python
from openapi_client.models.models_generate_config_file_request import ModelsGenerateConfigFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsGenerateConfigFileRequest from a JSON string
models_generate_config_file_request_instance = ModelsGenerateConfigFileRequest.from_json(json)
# print the JSON string representation of the object
print(ModelsGenerateConfigFileRequest.to_json())

# convert the object into a dict
models_generate_config_file_request_dict = models_generate_config_file_request_instance.to_dict()
# create an instance of ModelsGenerateConfigFileRequest from a dict
models_generate_config_file_request_from_dict = ModelsGenerateConfigFileRequest.from_dict(models_generate_config_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


