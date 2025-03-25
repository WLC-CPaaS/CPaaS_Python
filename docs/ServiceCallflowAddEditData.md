# ServiceCallflowAddEditData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featurecode** | [**ServiceFeatureCode**](ServiceFeatureCode.md) |  | [optional] 
**flow** | [**ServiceCallflowAddEditFlowData**](ServiceCallflowAddEditFlowData.md) |  | [optional] 
**name** | **str** |  | [optional] 
**numbers** | **List[str]** |  | 
**patterns** | **List[str]** |  | 

## Example

```python
from openapi_client.models.service_callflow_add_edit_data import ServiceCallflowAddEditData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallflowAddEditData from a JSON string
service_callflow_add_edit_data_instance = ServiceCallflowAddEditData.from_json(json)
# print the JSON string representation of the object
print(ServiceCallflowAddEditData.to_json())

# convert the object into a dict
service_callflow_add_edit_data_dict = service_callflow_add_edit_data_instance.to_dict()
# create an instance of ServiceCallflowAddEditData from a dict
service_callflow_add_edit_data_from_dict = ServiceCallflowAddEditData.from_dict(service_callflow_add_edit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


