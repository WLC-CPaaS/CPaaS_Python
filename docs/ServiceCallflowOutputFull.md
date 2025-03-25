# ServiceCallflowOutputFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featurecode** | [**ServiceFeatureCode**](ServiceFeatureCode.md) |  | [optional] 
**flow** | [**ServiceCallflowAddEditFlowData**](ServiceCallflowAddEditFlowData.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**numbers** | **List[str]** |  | 
**patterns** | **List[str]** |  | 

## Example

```python
from openapi_client.models.service_callflow_output_full import ServiceCallflowOutputFull

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallflowOutputFull from a JSON string
service_callflow_output_full_instance = ServiceCallflowOutputFull.from_json(json)
# print the JSON string representation of the object
print(ServiceCallflowOutputFull.to_json())

# convert the object into a dict
service_callflow_output_full_dict = service_callflow_output_full_instance.to_dict()
# create an instance of ServiceCallflowOutputFull from a dict
service_callflow_output_full_from_dict = ServiceCallflowOutputFull.from_dict(service_callflow_output_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


