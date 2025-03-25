# ServiceDocsAdminUserDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceAdminUserDeleteOutput**](ServiceAdminUserDeleteOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_admin_user_delete import ServiceDocsAdminUserDelete

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsAdminUserDelete from a JSON string
service_docs_admin_user_delete_instance = ServiceDocsAdminUserDelete.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsAdminUserDelete.to_json())

# convert the object into a dict
service_docs_admin_user_delete_dict = service_docs_admin_user_delete_instance.to_dict()
# create an instance of ServiceDocsAdminUserDelete from a dict
service_docs_admin_user_delete_from_dict = ServiceDocsAdminUserDelete.from_dict(service_docs_admin_user_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


