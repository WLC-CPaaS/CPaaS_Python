# ServiceVOIPCallQueueAddEditData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_wrapup_time** | **int** |  | [optional] 
**features** | **Dict[str, object]** |  | [optional] 
**force_away_on_reject** | **bool** |  | [optional] 
**name** | **str** |  | 
**queue_router** | **str** |  | [optional] 
**queue_type** | **str** |  | [optional] 
**ring_timeout** | **int** |  | [optional] 
**tick_time** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_call_queue_add_edit_data import ServiceVOIPCallQueueAddEditData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPCallQueueAddEditData from a JSON string
service_voip_call_queue_add_edit_data_instance = ServiceVOIPCallQueueAddEditData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPCallQueueAddEditData.to_json())

# convert the object into a dict
service_voip_call_queue_add_edit_data_dict = service_voip_call_queue_add_edit_data_instance.to_dict()
# create an instance of ServiceVOIPCallQueueAddEditData from a dict
service_voip_call_queue_add_edit_data_from_dict = ServiceVOIPCallQueueAddEditData.from_dict(service_voip_call_queue_add_edit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


