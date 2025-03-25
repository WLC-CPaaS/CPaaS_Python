# ServiceDocsWebhookGetAll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ModelAccountWebhook]**](ModelAccountWebhook.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_webhook_get_all import ServiceDocsWebhookGetAll

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsWebhookGetAll from a JSON string
service_docs_webhook_get_all_instance = ServiceDocsWebhookGetAll.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsWebhookGetAll.to_json())

# convert the object into a dict
service_docs_webhook_get_all_dict = service_docs_webhook_get_all_instance.to_dict()
# create an instance of ServiceDocsWebhookGetAll from a dict
service_docs_webhook_get_all_from_dict = ServiceDocsWebhookGetAll.from_dict(service_docs_webhook_get_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


