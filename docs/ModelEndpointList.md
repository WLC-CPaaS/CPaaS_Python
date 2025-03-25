# ModelEndpointList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**endpoint_name** | **str** |  | [optional] 
**feature_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_endpoint_list import ModelEndpointList

# TODO update the JSON string below
json = "{}"
# create an instance of ModelEndpointList from a JSON string
model_endpoint_list_instance = ModelEndpointList.from_json(json)
# print the JSON string representation of the object
print(ModelEndpointList.to_json())

# convert the object into a dict
model_endpoint_list_dict = model_endpoint_list_instance.to_dict()
# create an instance of ModelEndpointList from a dict
model_endpoint_list_from_dict = ModelEndpointList.from_dict(model_endpoint_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


