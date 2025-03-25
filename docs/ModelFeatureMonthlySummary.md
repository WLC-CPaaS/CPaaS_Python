# ModelFeatureMonthlySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**feature_count** | **int** |  | [optional] 
**feature_name** | **str** |  | [optional] 
**transaction_month** | **int** |  | [optional] 
**transaction_year** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.model_feature_monthly_summary import ModelFeatureMonthlySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ModelFeatureMonthlySummary from a JSON string
model_feature_monthly_summary_instance = ModelFeatureMonthlySummary.from_json(json)
# print the JSON string representation of the object
print(ModelFeatureMonthlySummary.to_json())

# convert the object into a dict
model_feature_monthly_summary_dict = model_feature_monthly_summary_instance.to_dict()
# create an instance of ModelFeatureMonthlySummary from a dict
model_feature_monthly_summary_from_dict = ModelFeatureMonthlySummary.from_dict(model_feature_monthly_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


