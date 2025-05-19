# ServiceCdrOutputShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizing_id** | **str** |  | [optional] 
**billing_seconds** | **int** |  | [optional] 
**bridge_id** | **str** |  | [optional] 
**call_id** | **str** |  | [optional] 
**call_priority** | **str** |  | [optional] 
**call_type** | **str** |  | [optional] 
**callee_id_name** | **str** |  | [optional] 
**callee_id_number** | **str** |  | [optional] 
**caller_id_name** | **str** |  | [optional] 
**caller_id_number** | **str** |  | [optional] 
**calling_from** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 
**dialed_number** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**duration_seconds** | **int** |  | [optional] 
**var_from** | **str** |  | [optional] 
**hangup_cause** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**interaction_id** | **str** |  | [optional] 
**media_recordings** | **List[object]** |  | [optional] 
**media_server** | **str** |  | [optional] 
**other_leg_call_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**rate** | **str** |  | [optional] 
**rate_name** | **str** |  | [optional] 
**recording_url** | **str** |  | [optional] 
**request** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**timestamp_datetime** | **str** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_cdr_output_short import ServiceCdrOutputShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCdrOutputShort from a JSON string
service_cdr_output_short_instance = ServiceCdrOutputShort.from_json(json)
# print the JSON string representation of the object
print(ServiceCdrOutputShort.to_json())

# convert the object into a dict
service_cdr_output_short_dict = service_cdr_output_short_instance.to_dict()
# create an instance of ServiceCdrOutputShort from a dict
service_cdr_output_short_from_dict = ServiceCdrOutputShort.from_dict(service_cdr_output_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


