# ServiceImpersonatedUserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**has_avatar** | **bool** |  | [optional] 
**last_name** | **str** |  | [optional] 
**priv_level** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_impersonated_user_info import ServiceImpersonatedUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceImpersonatedUserInfo from a JSON string
service_impersonated_user_info_instance = ServiceImpersonatedUserInfo.from_json(json)
# print the JSON string representation of the object
print(ServiceImpersonatedUserInfo.to_json())

# convert the object into a dict
service_impersonated_user_info_dict = service_impersonated_user_info_instance.to_dict()
# create an instance of ServiceImpersonatedUserInfo from a dict
service_impersonated_user_info_from_dict = ServiceImpersonatedUserInfo.from_dict(service_impersonated_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


