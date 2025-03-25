# ServiceDocsCallQueueResponseShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_call_queue_response_short import ServiceDocsCallQueueResponseShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsCallQueueResponseShort from a JSON string
service_docs_call_queue_response_short_instance = ServiceDocsCallQueueResponseShort.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsCallQueueResponseShort.to_json())

# convert the object into a dict
service_docs_call_queue_response_short_dict = service_docs_call_queue_response_short_instance.to_dict()
# create an instance of ServiceDocsCallQueueResponseShort from a dict
service_docs_call_queue_response_short_from_dict = ServiceDocsCallQueueResponseShort.from_dict(service_docs_call_queue_response_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


