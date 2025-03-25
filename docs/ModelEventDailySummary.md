# ModelEventDailySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**component** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**transaction_count** | **int** |  | [optional] 
**transaction_date** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_event_daily_summary import ModelEventDailySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ModelEventDailySummary from a JSON string
model_event_daily_summary_instance = ModelEventDailySummary.from_json(json)
# print the JSON string representation of the object
print(ModelEventDailySummary.to_json())

# convert the object into a dict
model_event_daily_summary_dict = model_event_daily_summary_instance.to_dict()
# create an instance of ModelEventDailySummary from a dict
model_event_daily_summary_from_dict = ModelEventDailySummary.from_dict(model_event_daily_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


