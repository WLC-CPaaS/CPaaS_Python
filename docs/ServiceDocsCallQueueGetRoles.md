# ServiceDocsCallQueueGetRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceCallQueueRolesOutput**](ServiceCallQueueRolesOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_call_queue_get_roles import ServiceDocsCallQueueGetRoles

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsCallQueueGetRoles from a JSON string
service_docs_call_queue_get_roles_instance = ServiceDocsCallQueueGetRoles.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsCallQueueGetRoles.to_json())

# convert the object into a dict
service_docs_call_queue_get_roles_dict = service_docs_call_queue_get_roles_instance.to_dict()
# create an instance of ServiceDocsCallQueueGetRoles from a dict
service_docs_call_queue_get_roles_from_dict = ServiceDocsCallQueueGetRoles.from_dict(service_docs_call_queue_get_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


