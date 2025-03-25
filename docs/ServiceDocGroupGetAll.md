# ServiceDocGroupGetAll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceGroupOutputShort**](ServiceGroupOutputShort.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_doc_group_get_all import ServiceDocGroupGetAll

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocGroupGetAll from a JSON string
service_doc_group_get_all_instance = ServiceDocGroupGetAll.from_json(json)
# print the JSON string representation of the object
print(ServiceDocGroupGetAll.to_json())

# convert the object into a dict
service_doc_group_get_all_dict = service_doc_group_get_all_instance.to_dict()
# create an instance of ServiceDocGroupGetAll from a dict
service_doc_group_get_all_from_dict = ServiceDocGroupGetAll.from_dict(service_doc_group_get_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


