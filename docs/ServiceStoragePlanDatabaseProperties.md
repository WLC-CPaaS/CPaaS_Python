# ServiceStoragePlanDatabaseProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_options** | **Dict[str, object]** |  | [optional] 
**names** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_storage_plan_database_properties import ServiceStoragePlanDatabaseProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStoragePlanDatabaseProperties from a JSON string
service_storage_plan_database_properties_instance = ServiceStoragePlanDatabaseProperties.from_json(json)
# print the JSON string representation of the object
print(ServiceStoragePlanDatabaseProperties.to_json())

# convert the object into a dict
service_storage_plan_database_properties_dict = service_storage_plan_database_properties_instance.to_dict()
# create an instance of ServiceStoragePlanDatabaseProperties from a dict
service_storage_plan_database_properties_from_dict = ServiceStoragePlanDatabaseProperties.from_dict(service_storage_plan_database_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


