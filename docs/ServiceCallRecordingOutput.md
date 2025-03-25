# ServiceCallRecordingOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** |  | [optional] 
**callee_id_name** | **str** |  | [optional] 
**callee_id_number** | **str** |  | [optional] 
**caller_id_name** | **str** |  | [optional] 
**caller_id_number** | **str** |  | [optional] 
**cdr_id** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**custom_channel_vars** | **Dict[str, object]** |  | [optional] 
**description** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**duration_ms** | **int** |  | [optional] 
**endpoint_id** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**interaction_id** | **str** |  | [optional] 
**media_source** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**request** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**start** | **int** |  | [optional] 
**to** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_call_recording_output import ServiceCallRecordingOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallRecordingOutput from a JSON string
service_call_recording_output_instance = ServiceCallRecordingOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceCallRecordingOutput.to_json())

# convert the object into a dict
service_call_recording_output_dict = service_call_recording_output_instance.to_dict()
# create an instance of ServiceCallRecordingOutput from a dict
service_call_recording_output_from_dict = ServiceCallRecordingOutput.from_dict(service_call_recording_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


