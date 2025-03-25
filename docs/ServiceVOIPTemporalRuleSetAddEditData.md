# ServiceVOIPTemporalRuleSetAddEditData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**temporal_rules** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_temporal_rule_set_add_edit_data import ServiceVOIPTemporalRuleSetAddEditData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPTemporalRuleSetAddEditData from a JSON string
service_voip_temporal_rule_set_add_edit_data_instance = ServiceVOIPTemporalRuleSetAddEditData.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPTemporalRuleSetAddEditData.to_json())

# convert the object into a dict
service_voip_temporal_rule_set_add_edit_data_dict = service_voip_temporal_rule_set_add_edit_data_instance.to_dict()
# create an instance of ServiceVOIPTemporalRuleSetAddEditData from a dict
service_voip_temporal_rule_set_add_edit_data_from_dict = ServiceVOIPTemporalRuleSetAddEditData.from_dict(service_voip_temporal_rule_set_add_edit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


