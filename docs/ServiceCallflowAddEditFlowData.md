# ServiceCallflowAddEditFlowData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**Dict[str, ServiceCallflowAddEditFlowData]**](ServiceCallflowAddEditFlowData.md) |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**module** | **str** |  | 

## Example

```python
from openapi_client.models.service_callflow_add_edit_flow_data import ServiceCallflowAddEditFlowData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCallflowAddEditFlowData from a JSON string
service_callflow_add_edit_flow_data_instance = ServiceCallflowAddEditFlowData.from_json(json)
# print the JSON string representation of the object
print(ServiceCallflowAddEditFlowData.to_json())

# convert the object into a dict
service_callflow_add_edit_flow_data_dict = service_callflow_add_edit_flow_data_instance.to_dict()
# create an instance of ServiceCallflowAddEditFlowData from a dict
service_callflow_add_edit_flow_data_from_dict = ServiceCallflowAddEditFlowData.from_dict(service_callflow_add_edit_flow_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


