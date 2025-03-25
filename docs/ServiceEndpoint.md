# ServiceEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_endpoint import ServiceEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEndpoint from a JSON string
service_endpoint_instance = ServiceEndpoint.from_json(json)
# print the JSON string representation of the object
print(ServiceEndpoint.to_json())

# convert the object into a dict
service_endpoint_dict = service_endpoint_instance.to_dict()
# create an instance of ServiceEndpoint from a dict
service_endpoint_from_dict = ServiceEndpoint.from_dict(service_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


