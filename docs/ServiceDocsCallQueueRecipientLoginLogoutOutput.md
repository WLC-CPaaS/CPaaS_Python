# ServiceDocsCallQueueRecipientLoginLogoutOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_call_queue_recipient_login_logout_output import ServiceDocsCallQueueRecipientLoginLogoutOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsCallQueueRecipientLoginLogoutOutput from a JSON string
service_docs_call_queue_recipient_login_logout_output_instance = ServiceDocsCallQueueRecipientLoginLogoutOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsCallQueueRecipientLoginLogoutOutput.to_json())

# convert the object into a dict
service_docs_call_queue_recipient_login_logout_output_dict = service_docs_call_queue_recipient_login_logout_output_instance.to_dict()
# create an instance of ServiceDocsCallQueueRecipientLoginLogoutOutput from a dict
service_docs_call_queue_recipient_login_logout_output_from_dict = ServiceDocsCallQueueRecipientLoginLogoutOutput.from_dict(service_docs_call_queue_recipient_login_logout_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


