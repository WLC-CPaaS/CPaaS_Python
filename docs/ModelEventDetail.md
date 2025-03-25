# ModelEventDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**component** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**exec_status** | **str** |  | [optional] 
**log_date** | **str** |  | [optional] 
**log_time** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_event_detail import ModelEventDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ModelEventDetail from a JSON string
model_event_detail_instance = ModelEventDetail.from_json(json)
# print the JSON string representation of the object
print(ModelEventDetail.to_json())

# convert the object into a dict
model_event_detail_dict = model_event_detail_instance.to_dict()
# create an instance of ModelEventDetail from a dict
model_event_detail_from_dict = ModelEventDetail.from_dict(model_event_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


