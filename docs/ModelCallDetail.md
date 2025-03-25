# ModelCallDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**call_duration** | **str** |  | [optional] 
**call_id** | **str** |  | [optional] 
**call_time** | **str** |  | [optional] 
**call_type** | **str** |  | [optional] 
**callee_name** | **str** |  | [optional] 
**callee_number** | **str** |  | [optional] 
**caller_name** | **str** |  | [optional] 
**caller_number** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_call_detail import ModelCallDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCallDetail from a JSON string
model_call_detail_instance = ModelCallDetail.from_json(json)
# print the JSON string representation of the object
print(ModelCallDetail.to_json())

# convert the object into a dict
model_call_detail_dict = model_call_detail_instance.to_dict()
# create an instance of ModelCallDetail from a dict
model_call_detail_from_dict = ModelCallDetail.from_dict(model_call_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


