# ServiceDocsChannelGetAll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceChannelOutput]**](ServiceChannelOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_channel_get_all import ServiceDocsChannelGetAll

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsChannelGetAll from a JSON string
service_docs_channel_get_all_instance = ServiceDocsChannelGetAll.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsChannelGetAll.to_json())

# convert the object into a dict
service_docs_channel_get_all_dict = service_docs_channel_get_all_instance.to_dict()
# create an instance of ServiceDocsChannelGetAll from a dict
service_docs_channel_get_all_from_dict = ServiceDocsChannelGetAll.from_dict(service_docs_channel_get_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


