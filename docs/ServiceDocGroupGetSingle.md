# ServiceDocGroupGetSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceGroupOutputFull**](ServiceGroupOutputFull.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_doc_group_get_single import ServiceDocGroupGetSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocGroupGetSingle from a JSON string
service_doc_group_get_single_instance = ServiceDocGroupGetSingle.from_json(json)
# print the JSON string representation of the object
print(ServiceDocGroupGetSingle.to_json())

# convert the object into a dict
service_doc_group_get_single_dict = service_doc_group_get_single_instance.to_dict()
# create an instance of ServiceDocGroupGetSingle from a dict
service_doc_group_get_single_from_dict = ServiceDocGroupGetSingle.from_dict(service_doc_group_get_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


