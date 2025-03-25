# ServiceStoragePlanDatabase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**ServiceStoragePlanDatabaseAttachment**](ServiceStoragePlanDatabaseAttachment.md) |  | [optional] 
**connection** | **str** |  | [optional] 
**database** | [**ServiceStoragePlanDatabaseProperties**](ServiceStoragePlanDatabaseProperties.md) |  | [optional] 
**types** | [**ServiceStoragePlanDatabaseTypes**](ServiceStoragePlanDatabaseTypes.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_storage_plan_database import ServiceStoragePlanDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStoragePlanDatabase from a JSON string
service_storage_plan_database_instance = ServiceStoragePlanDatabase.from_json(json)
# print the JSON string representation of the object
print(ServiceStoragePlanDatabase.to_json())

# convert the object into a dict
service_storage_plan_database_dict = service_storage_plan_database_instance.to_dict()
# create an instance of ServiceStoragePlanDatabase from a dict
service_storage_plan_database_from_dict = ServiceStoragePlanDatabase.from_dict(service_storage_plan_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


