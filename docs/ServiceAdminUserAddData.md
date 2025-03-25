# ServiceAdminUserAddData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from openapi_client.models.service_admin_user_add_data import ServiceAdminUserAddData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAdminUserAddData from a JSON string
service_admin_user_add_data_instance = ServiceAdminUserAddData.from_json(json)
# print the JSON string representation of the object
print(ServiceAdminUserAddData.to_json())

# convert the object into a dict
service_admin_user_add_data_dict = service_admin_user_add_data_instance.to_dict()
# create an instance of ServiceAdminUserAddData from a dict
service_admin_user_add_data_from_dict = ServiceAdminUserAddData.from_dict(service_admin_user_add_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


