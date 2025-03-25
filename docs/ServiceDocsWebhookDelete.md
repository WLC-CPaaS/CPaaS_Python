# ServiceDocsWebhookDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceWebhookDeleteOutput**](ServiceWebhookDeleteOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_webhook_delete import ServiceDocsWebhookDelete

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsWebhookDelete from a JSON string
service_docs_webhook_delete_instance = ServiceDocsWebhookDelete.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsWebhookDelete.to_json())

# convert the object into a dict
service_docs_webhook_delete_dict = service_docs_webhook_delete_instance.to_dict()
# create an instance of ServiceDocsWebhookDelete from a dict
service_docs_webhook_delete_from_dict = ServiceDocsWebhookDelete.from_dict(service_docs_webhook_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


