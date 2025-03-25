# ServiceVOIPTemporalRuleAddEdit2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle** | **str** |  | 
**days** | **List[int]** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**interval** | **int** |  | [optional] 
**month** | **int** |  | [optional] 
**name** | **str** |  | 
**ordinal** | **str** |  | [optional] 
**start_date** | **int** |  | [optional] 
**start_date_req** | **str** |  | [optional] 
**time_window_start** | **int** |  | [optional] 
**time_window_start_req** | **str** |  | [optional] 
**time_window_stop** | **int** |  | [optional] 
**time_window_stop_req** | **str** |  | [optional] 
**wdays** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_temporal_rule_add_edit2 import ServiceVOIPTemporalRuleAddEdit2

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPTemporalRuleAddEdit2 from a JSON string
service_voip_temporal_rule_add_edit2_instance = ServiceVOIPTemporalRuleAddEdit2.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPTemporalRuleAddEdit2.to_json())

# convert the object into a dict
service_voip_temporal_rule_add_edit2_dict = service_voip_temporal_rule_add_edit2_instance.to_dict()
# create an instance of ServiceVOIPTemporalRuleAddEdit2 from a dict
service_voip_temporal_rule_add_edit2_from_dict = ServiceVOIPTemporalRuleAddEdit2.from_dict(service_voip_temporal_rule_add_edit2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


