# ServiceImpersonateUserOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**auth_token** | **str** |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**is_master_account** | **bool** |  | [optional] 
**is_reseller** | **bool** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**reseller_id** | **str** |  | [optional] 
**user_info** | [**ServiceImpersonatedUserInfo**](ServiceImpersonatedUserInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_impersonate_user_output_full import ServiceImpersonateUserOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceImpersonateUserOutputFull from a JSON string
service_impersonate_user_output_full_instance = ServiceImpersonateUserOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceImpersonateUserOutputFull.to_json())

# convert the object into a dict
service_impersonate_user_output_full_dict = service_impersonate_user_output_full_instance.to_dict()
# create an instance of ServiceImpersonateUserOutputFull from a dict
service_impersonate_user_output_full_from_dict = ServiceImpersonateUserOutputFull.from_dict(service_impersonate_user_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


