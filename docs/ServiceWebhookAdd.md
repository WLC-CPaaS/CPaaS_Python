# ServiceWebhookAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_method** | **str** |  | 
**callback_url** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**title** | **str** |  | 
**webhook_type** | **str** |  | 

## Example

```python
from openapi_client.models.service_webhook_add import ServiceWebhookAdd

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceWebhookAdd from a JSON string
service_webhook_add_instance = ServiceWebhookAdd.from_json(json)
# print the JSON string representation of the object
print(ServiceWebhookAdd.to_json())

# convert the object into a dict
service_webhook_add_dict = service_webhook_add_instance.to_dict()
# create an instance of ServiceWebhookAdd from a dict
service_webhook_add_from_dict = ServiceWebhookAdd.from_dict(service_webhook_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


