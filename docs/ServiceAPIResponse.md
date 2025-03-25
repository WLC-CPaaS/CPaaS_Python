# ServiceAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | Data payload | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_api_response import ServiceAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAPIResponse from a JSON string
service_api_response_instance = ServiceAPIResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceAPIResponse.to_json())

# convert the object into a dict
service_api_response_dict = service_api_response_instance.to_dict()
# create an instance of ServiceAPIResponse from a dict
service_api_response_from_dict = ServiceAPIResponse.from_dict(service_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


