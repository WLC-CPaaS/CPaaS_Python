# ServiceVOIPImpersonateUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_impersonate_user import ServiceVOIPImpersonateUser

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPImpersonateUser from a JSON string
service_voip_impersonate_user_instance = ServiceVOIPImpersonateUser.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPImpersonateUser.to_json())

# convert the object into a dict
service_voip_impersonate_user_dict = service_voip_impersonate_user_instance.to_dict()
# create an instance of ServiceVOIPImpersonateUser from a dict
service_voip_impersonate_user_from_dict = ServiceVOIPImpersonateUser.from_dict(service_voip_impersonate_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


