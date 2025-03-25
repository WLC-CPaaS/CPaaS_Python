# ServiceAdminUserOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_admin_user_output import ServiceAdminUserOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAdminUserOutput from a JSON string
service_admin_user_output_instance = ServiceAdminUserOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceAdminUserOutput.to_json())

# convert the object into a dict
service_admin_user_output_dict = service_admin_user_output_instance.to_dict()
# create an instance of ServiceAdminUserOutput from a dict
service_admin_user_output_from_dict = ServiceAdminUserOutput.from_dict(service_admin_user_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


