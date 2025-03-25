# ServiceCallQueueStatusOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_recipient_count** | **int** |  | [optional] 
**available_recipient_count** | **int** |  | [optional] 
**node** | **str** |  | [optional] 
**stats** | [**ServiceCallQueueStatusStats**](ServiceCallQueueStatusStats.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_call_queue_status_output import ServiceCallQueueStatusOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallQueueStatusOutput from a JSON string
service_call_queue_status_output_instance = ServiceCallQueueStatusOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceCallQueueStatusOutput.to_json())

# convert the object into a dict
service_call_queue_status_output_dict = service_call_queue_status_output_instance.to_dict()
# create an instance of ServiceCallQueueStatusOutput from a dict
service_call_queue_status_output_from_dict = ServiceCallQueueStatusOutput.from_dict(service_call_queue_status_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


