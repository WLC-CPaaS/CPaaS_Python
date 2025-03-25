# ServiceQueueRecipientOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**recipient** | [**ServiceQueueRecipientOutputFullRecipient**](ServiceQueueRecipientOutputFullRecipient.md) |  | [optional] 
**roles** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_queue_recipient_output_full import ServiceQueueRecipientOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQueueRecipientOutputFull from a JSON string
service_queue_recipient_output_full_instance = ServiceQueueRecipientOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceQueueRecipientOutputFull.to_json())

# convert the object into a dict
service_queue_recipient_output_full_dict = service_queue_recipient_output_full_instance.to_dict()
# create an instance of ServiceQueueRecipientOutputFull from a dict
service_queue_recipient_output_full_from_dict = ServiceQueueRecipientOutputFull.from_dict(service_queue_recipient_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


