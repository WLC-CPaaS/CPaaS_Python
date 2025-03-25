# ServiceTemporalRuleOutputShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_temporal_rule_output_short import ServiceTemporalRuleOutputShort

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTemporalRuleOutputShort from a JSON string
service_temporal_rule_output_short_instance = ServiceTemporalRuleOutputShort.from_json(json)
# print the JSON string representation of the object
print(ServiceTemporalRuleOutputShort.to_json())

# convert the object into a dict
service_temporal_rule_output_short_dict = service_temporal_rule_output_short_instance.to_dict()
# create an instance of ServiceTemporalRuleOutputShort from a dict
service_temporal_rule_output_short_from_dict = ServiceTemporalRuleOutputShort.from_dict(service_temporal_rule_output_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


