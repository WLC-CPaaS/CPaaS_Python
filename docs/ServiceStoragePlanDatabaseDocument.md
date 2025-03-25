# ServiceStoragePlanDatabaseDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**ServiceStoragePlanDatabaseAttachment**](ServiceStoragePlanDatabaseAttachment.md) |  | [optional] 
**connection** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_storage_plan_database_document import ServiceStoragePlanDatabaseDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStoragePlanDatabaseDocument from a JSON string
service_storage_plan_database_document_instance = ServiceStoragePlanDatabaseDocument.from_json(json)
# print the JSON string representation of the object
print(ServiceStoragePlanDatabaseDocument.to_json())

# convert the object into a dict
service_storage_plan_database_document_dict = service_storage_plan_database_document_instance.to_dict()
# create an instance of ServiceStoragePlanDatabaseDocument from a dict
service_storage_plan_database_document_from_dict = ServiceStoragePlanDatabaseDocument.from_dict(service_storage_plan_database_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


