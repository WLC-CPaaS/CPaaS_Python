# ResponseProvisionError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** | Error Code | [optional] 
**errors** | **List[object]** | Error details | [optional] 
**message** | **str** | Error Message | [optional] 
**request_id** | **str** | Request ID | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.response_provision_error import ResponseProvisionError

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseProvisionError from a JSON string
response_provision_error_instance = ResponseProvisionError.from_json(json)
# print the JSON string representation of the object
print(ResponseProvisionError.to_json())

# convert the object into a dict
response_provision_error_dict = response_provision_error_instance.to_dict()
# create an instance of ResponseProvisionError from a dict
response_provision_error_from_dict = ResponseProvisionError.from_dict(response_provision_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


