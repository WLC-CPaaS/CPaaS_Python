# ServiceDocsStorageGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceStorageOutput**](ServiceStorageOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_storage_get import ServiceDocsStorageGet

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsStorageGet from a JSON string
service_docs_storage_get_instance = ServiceDocsStorageGet.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsStorageGet.to_json())

# convert the object into a dict
service_docs_storage_get_dict = service_docs_storage_get_instance.to_dict()
# create an instance of ServiceDocsStorageGet from a dict
service_docs_storage_get_from_dict = ServiceDocsStorageGet.from_dict(service_docs_storage_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


