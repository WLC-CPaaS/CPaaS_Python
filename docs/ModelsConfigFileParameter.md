# ModelsConfigFileParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension** | **str** |  | [optional] 
**https_host** | **str** |  | [optional] 
**https_password** | **str** |  | [optional] 
**https_username** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**realm** | **str** |  | [optional] 
**sip_password** | **str** |  | [optional] 
**sip_username** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**voicemail_box_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.models_config_file_parameter import ModelsConfigFileParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsConfigFileParameter from a JSON string
models_config_file_parameter_instance = ModelsConfigFileParameter.from_json(json)
# print the JSON string representation of the object
print(ModelsConfigFileParameter.to_json())

# convert the object into a dict
models_config_file_parameter_dict = models_config_file_parameter_instance.to_dict()
# create an instance of ModelsConfigFileParameter from a dict
models_config_file_parameter_from_dict = ModelsConfigFileParameter.from_dict(models_config_file_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


