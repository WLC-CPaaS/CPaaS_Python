# ServiceTemporalRuleOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle** | **str** |  | [optional] 
**days** | **List[int]** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**interval** | **int** |  | [optional] 
**month** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**ordinal** | **str** |  | [optional] 
**start_date** | **int** |  | [optional] 
**time_window_start** | **int** |  | [optional] 
**time_window_stop** | **int** |  | [optional] 
**wdays** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_temporal_rule_output_full import ServiceTemporalRuleOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTemporalRuleOutputFull from a JSON string
service_temporal_rule_output_full_instance = ServiceTemporalRuleOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceTemporalRuleOutputFull.to_json())

# convert the object into a dict
service_temporal_rule_output_full_dict = service_temporal_rule_output_full_instance.to_dict()
# create an instance of ServiceTemporalRuleOutputFull from a dict
service_temporal_rule_output_full_from_dict = ServiceTemporalRuleOutputFull.from_dict(service_temporal_rule_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


