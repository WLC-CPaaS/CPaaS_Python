# ServiceCallQueueStatusStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned_sessions** | **int** |  | [optional] 
**active_session_count** | **int** |  | [optional] 
**average_wait** | **int** |  | [optional] 
**estimated_wait** | **int** |  | [optional] 
**longest_wait** | **int** |  | [optional] 
**missed_sessions** | **int** |  | [optional] 
**recipient_count** | **int** |  | [optional] 
**total_sessions** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.service_call_queue_status_stats import ServiceCallQueueStatusStats

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallQueueStatusStats from a JSON string
service_call_queue_status_stats_instance = ServiceCallQueueStatusStats.from_json(json)
# print the JSON string representation of the object
print(ServiceCallQueueStatusStats.to_json())

# convert the object into a dict
service_call_queue_status_stats_dict = service_call_queue_status_stats_instance.to_dict()
# create an instance of ServiceCallQueueStatusStats from a dict
service_call_queue_status_stats_from_dict = ServiceCallQueueStatusStats.from_dict(service_call_queue_status_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


