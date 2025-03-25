# ServiceStorageOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **Dict[str, object]** |  | [optional] 
**connections** | **Dict[str, object]** |  | [optional] 
**id** | **str** |  | [optional] 
**plan** | [**ServiceStoragePlan**](ServiceStoragePlan.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_storage_output import ServiceStorageOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStorageOutput from a JSON string
service_storage_output_instance = ServiceStorageOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceStorageOutput.to_json())

# convert the object into a dict
service_storage_output_dict = service_storage_output_instance.to_dict()
# create an instance of ServiceStorageOutput from a dict
service_storage_output_from_dict = ServiceStorageOutput.from_dict(service_storage_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


