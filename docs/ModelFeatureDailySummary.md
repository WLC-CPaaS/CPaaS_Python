# ModelFeatureDailySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**feature_count** | **int** |  | [optional] 
**feature_name** | **str** |  | [optional] 
**log_date** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_feature_daily_summary import ModelFeatureDailySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ModelFeatureDailySummary from a JSON string
model_feature_daily_summary_instance = ModelFeatureDailySummary.from_json(json)
# print the JSON string representation of the object
print(ModelFeatureDailySummary.to_json())

# convert the object into a dict
model_feature_daily_summary_dict = model_feature_daily_summary_instance.to_dict()
# create an instance of ModelFeatureDailySummary from a dict
model_feature_daily_summary_from_dict = ModelFeatureDailySummary.from_dict(model_feature_daily_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


