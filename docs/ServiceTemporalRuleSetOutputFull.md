# ServiceTemporalRuleSetOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**temporal_rules** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_temporal_rule_set_output_full import ServiceTemporalRuleSetOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTemporalRuleSetOutputFull from a JSON string
service_temporal_rule_set_output_full_instance = ServiceTemporalRuleSetOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceTemporalRuleSetOutputFull.to_json())

# convert the object into a dict
service_temporal_rule_set_output_full_dict = service_temporal_rule_set_output_full_instance.to_dict()
# create an instance of ServiceTemporalRuleSetOutputFull from a dict
service_temporal_rule_set_output_full_from_dict = ServiceTemporalRuleSetOutputFull.from_dict(service_temporal_rule_set_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


