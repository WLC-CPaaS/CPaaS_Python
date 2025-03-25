# ServiceAPIResponseStatusCodeOnly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.service_api_response_status_code_only import ServiceAPIResponseStatusCodeOnly

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAPIResponseStatusCodeOnly from a JSON string
service_api_response_status_code_only_instance = ServiceAPIResponseStatusCodeOnly.from_json(json)
# print the JSON string representation of the object
print(ServiceAPIResponseStatusCodeOnly.to_json())

# convert the object into a dict
service_api_response_status_code_only_dict = service_api_response_status_code_only_instance.to_dict()
# create an instance of ServiceAPIResponseStatusCodeOnly from a dict
service_api_response_status_code_only_from_dict = ServiceAPIResponseStatusCodeOnly.from_dict(service_api_response_status_code_only_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


