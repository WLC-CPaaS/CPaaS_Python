# ServiceDocsUserGetSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceUserOutputFull**](ServiceUserOutputFull.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_user_get_single import ServiceDocsUserGetSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsUserGetSingle from a JSON string
service_docs_user_get_single_instance = ServiceDocsUserGetSingle.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsUserGetSingle.to_json())

# convert the object into a dict
service_docs_user_get_single_dict = service_docs_user_get_single_instance.to_dict()
# create an instance of ServiceDocsUserGetSingle from a dict
service_docs_user_get_single_from_dict = ServiceDocsUserGetSingle.from_dict(service_docs_user_get_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


