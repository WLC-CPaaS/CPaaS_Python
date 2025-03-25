# ServiceDocsCallQueueGetSingleStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceCallQueueStatusOutput**](ServiceCallQueueStatusOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_call_queue_get_single_status import ServiceDocsCallQueueGetSingleStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsCallQueueGetSingleStatus from a JSON string
service_docs_call_queue_get_single_status_instance = ServiceDocsCallQueueGetSingleStatus.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsCallQueueGetSingleStatus.to_json())

# convert the object into a dict
service_docs_call_queue_get_single_status_dict = service_docs_call_queue_get_single_status_instance.to_dict()
# create an instance of ServiceDocsCallQueueGetSingleStatus from a dict
service_docs_call_queue_get_single_status_from_dict = ServiceDocsCallQueueGetSingleStatus.from_dict(service_docs_call_queue_get_single_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


