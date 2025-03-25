# ServiceDocsAdminUserGetAll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceAdminUserOutput]**](ServiceAdminUserOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_admin_user_get_all import ServiceDocsAdminUserGetAll

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsAdminUserGetAll from a JSON string
service_docs_admin_user_get_all_instance = ServiceDocsAdminUserGetAll.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsAdminUserGetAll.to_json())

# convert the object into a dict
service_docs_admin_user_get_all_dict = service_docs_admin_user_get_all_instance.to_dict()
# create an instance of ServiceDocsAdminUserGetAll from a dict
service_docs_admin_user_get_all_from_dict = ServiceDocsAdminUserGetAll.from_dict(service_docs_admin_user_get_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


