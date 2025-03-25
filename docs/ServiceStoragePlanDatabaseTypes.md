# ServiceStoragePlanDatabaseTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_recording** | [**ServiceStoragePlanDatabaseDocument**](ServiceStoragePlanDatabaseDocument.md) |  | [optional] 
**fax** | [**ServiceStoragePlanDatabaseDocument**](ServiceStoragePlanDatabaseDocument.md) |  | [optional] 
**function** | [**ServiceStoragePlanDatabaseDocument**](ServiceStoragePlanDatabaseDocument.md) |  | [optional] 
**mailbox_message** | [**ServiceStoragePlanDatabaseDocument**](ServiceStoragePlanDatabaseDocument.md) |  | [optional] 
**media** | [**ServiceStoragePlanDatabaseDocument**](ServiceStoragePlanDatabaseDocument.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_storage_plan_database_types import ServiceStoragePlanDatabaseTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStoragePlanDatabaseTypes from a JSON string
service_storage_plan_database_types_instance = ServiceStoragePlanDatabaseTypes.from_json(json)
# print the JSON string representation of the object
print(ServiceStoragePlanDatabaseTypes.to_json())

# convert the object into a dict
service_storage_plan_database_types_dict = service_storage_plan_database_types_instance.to_dict()
# create an instance of ServiceStoragePlanDatabaseTypes from a dict
service_storage_plan_database_types_from_dict = ServiceStoragePlanDatabaseTypes.from_dict(service_storage_plan_database_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


