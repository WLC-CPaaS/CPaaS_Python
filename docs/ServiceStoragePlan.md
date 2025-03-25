# ServiceStoragePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**ServiceStoragePlanDatabase**](ServiceStoragePlanDatabase.md) |  | [optional] 
**aggregate** | [**ServiceStoragePlanDatabase**](ServiceStoragePlanDatabase.md) |  | [optional] 
**modb** | [**ServiceStoragePlanDatabase**](ServiceStoragePlanDatabase.md) |  | [optional] 
**system** | [**ServiceStoragePlanDatabase**](ServiceStoragePlanDatabase.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_storage_plan import ServiceStoragePlan

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStoragePlan from a JSON string
service_storage_plan_instance = ServiceStoragePlan.from_json(json)
# print the JSON string representation of the object
print(ServiceStoragePlan.to_json())

# convert the object into a dict
service_storage_plan_dict = service_storage_plan_instance.to_dict()
# create an instance of ServiceStoragePlan from a dict
service_storage_plan_from_dict = ServiceStoragePlan.from_dict(service_storage_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


