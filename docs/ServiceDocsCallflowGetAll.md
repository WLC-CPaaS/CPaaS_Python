# ServiceDocsCallflowGetAll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceCallflowOutputShort**](ServiceCallflowOutputShort.md) |  | [optional] 
**next_start_key** | **str** | List Pagination: Used to get the next page of results. Will not exist if this is the last page. | [optional] 
**page_size** | **int** | List Pagination: The number of results returned in this page | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**start_key** | **str** | List Pagination: Code for paged results | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_callflow_get_all import ServiceDocsCallflowGetAll

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsCallflowGetAll from a JSON string
service_docs_callflow_get_all_instance = ServiceDocsCallflowGetAll.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsCallflowGetAll.to_json())

# convert the object into a dict
service_docs_callflow_get_all_dict = service_docs_callflow_get_all_instance.to_dict()
# create an instance of ServiceDocsCallflowGetAll from a dict
service_docs_callflow_get_all_from_dict = ServiceDocsCallflowGetAll.from_dict(service_docs_callflow_get_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


