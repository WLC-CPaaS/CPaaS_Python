# ModelCallDailySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**call_date** | **str** |  | [optional] 
**call_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**total_call_duration** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_call_daily_summary import ModelCallDailySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCallDailySummary from a JSON string
model_call_daily_summary_instance = ModelCallDailySummary.from_json(json)
# print the JSON string representation of the object
print(ModelCallDailySummary.to_json())

# convert the object into a dict
model_call_daily_summary_dict = model_call_daily_summary_instance.to_dict()
# create an instance of ModelCallDailySummary from a dict
model_call_daily_summary_from_dict = ModelCallDailySummary.from_dict(model_call_daily_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


