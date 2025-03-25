# ServiceStoragePlanDatabaseAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handler** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 
**stub** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.service_storage_plan_database_attachment import ServiceStoragePlanDatabaseAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStoragePlanDatabaseAttachment from a JSON string
service_storage_plan_database_attachment_instance = ServiceStoragePlanDatabaseAttachment.from_json(json)
# print the JSON string representation of the object
print(ServiceStoragePlanDatabaseAttachment.to_json())

# convert the object into a dict
service_storage_plan_database_attachment_dict = service_storage_plan_database_attachment_instance.to_dict()
# create an instance of ServiceStoragePlanDatabaseAttachment from a dict
service_storage_plan_database_attachment_from_dict = ServiceStoragePlanDatabaseAttachment.from_dict(service_storage_plan_database_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


