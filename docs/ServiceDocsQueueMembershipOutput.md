# ServiceDocsQueueMembershipOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_queue_membership_output import ServiceDocsQueueMembershipOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsQueueMembershipOutput from a JSON string
service_docs_queue_membership_output_instance = ServiceDocsQueueMembershipOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsQueueMembershipOutput.to_json())

# convert the object into a dict
service_docs_queue_membership_output_dict = service_docs_queue_membership_output_instance.to_dict()
# create an instance of ServiceDocsQueueMembershipOutput from a dict
service_docs_queue_membership_output_from_dict = ServiceDocsQueueMembershipOutput.from_dict(service_docs_queue_membership_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


