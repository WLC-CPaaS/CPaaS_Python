# ServiceDocsMetaflowGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceMetaflowOutput**](ServiceMetaflowOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_metaflow_get import ServiceDocsMetaflowGet

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsMetaflowGet from a JSON string
service_docs_metaflow_get_instance = ServiceDocsMetaflowGet.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsMetaflowGet.to_json())

# convert the object into a dict
service_docs_metaflow_get_dict = service_docs_metaflow_get_instance.to_dict()
# create an instance of ServiceDocsMetaflowGet from a dict
service_docs_metaflow_get_from_dict = ServiceDocsMetaflowGet.from_dict(service_docs_metaflow_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


