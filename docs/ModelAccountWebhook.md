# ModelAccountWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**callback_method** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**webhook_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_account_webhook import ModelAccountWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAccountWebhook from a JSON string
model_account_webhook_instance = ModelAccountWebhook.from_json(json)
# print the JSON string representation of the object
print(ModelAccountWebhook.to_json())

# convert the object into a dict
model_account_webhook_dict = model_account_webhook_instance.to_dict()
# create an instance of ModelAccountWebhook from a dict
model_account_webhook_from_dict = ModelAccountWebhook.from_dict(model_account_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


