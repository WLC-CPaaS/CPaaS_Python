# ServiceQueueRecipientOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**recipient** | [**ServiceQueueRecipientOutputRecipient**](ServiceQueueRecipientOutputRecipient.md) |  | [optional] 
**roles** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_queue_recipient_output import ServiceQueueRecipientOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQueueRecipientOutput from a JSON string
service_queue_recipient_output_instance = ServiceQueueRecipientOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceQueueRecipientOutput.to_json())

# convert the object into a dict
service_queue_recipient_output_dict = service_queue_recipient_output_instance.to_dict()
# create an instance of ServiceQueueRecipientOutput from a dict
service_queue_recipient_output_from_dict = ServiceQueueRecipientOutput.from_dict(service_queue_recipient_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


