# ServiceCallQueueOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_wrapup_time** | **int** |  | [optional] 
**features** | **Dict[str, object]** |  | [optional] 
**force_away_on_reject** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**queue_router** | **str** |  | [optional] 
**queue_type** | **str** |  | [optional] 
**ring_timeout** | **int** |  | [optional] 
**tick_time** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.service_call_queue_output_full import ServiceCallQueueOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallQueueOutputFull from a JSON string
service_call_queue_output_full_instance = ServiceCallQueueOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceCallQueueOutputFull.to_json())

# convert the object into a dict
service_call_queue_output_full_dict = service_call_queue_output_full_instance.to_dict()
# create an instance of ServiceCallQueueOutputFull from a dict
service_call_queue_output_full_from_dict = ServiceCallQueueOutputFull.from_dict(service_call_queue_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


