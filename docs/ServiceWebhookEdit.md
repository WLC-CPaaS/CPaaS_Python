# ServiceWebhookEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_method** | **str** |  | 
**callback_url** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**title** | **str** |  | 
**webhook_type** | **str** |  | 

## Example

```python
from openapi_client.models.service_webhook_edit import ServiceWebhookEdit

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceWebhookEdit from a JSON string
service_webhook_edit_instance = ServiceWebhookEdit.from_json(json)
# print the JSON string representation of the object
print(ServiceWebhookEdit.to_json())

# convert the object into a dict
service_webhook_edit_dict = service_webhook_edit_instance.to_dict()
# create an instance of ServiceWebhookEdit from a dict
service_webhook_edit_from_dict = ServiceWebhookEdit.from_dict(service_webhook_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


