# ServiceDocsSystemStatusGetSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceSystemStatusOutput**](ServiceSystemStatusOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 
**system_status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_docs_system_status_get_single import ServiceDocsSystemStatusGetSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsSystemStatusGetSingle from a JSON string
service_docs_system_status_get_single_instance = ServiceDocsSystemStatusGetSingle.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsSystemStatusGetSingle.to_json())

# convert the object into a dict
service_docs_system_status_get_single_dict = service_docs_system_status_get_single_instance.to_dict()
# create an instance of ServiceDocsSystemStatusGetSingle from a dict
service_docs_system_status_get_single_from_dict = ServiceDocsSystemStatusGetSingle.from_dict(service_docs_system_status_get_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


