# ServiceAPIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_api_key import ServiceAPIKey

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAPIKey from a JSON string
service_api_key_instance = ServiceAPIKey.from_json(json)
# print the JSON string representation of the object
print(ServiceAPIKey.to_json())

# convert the object into a dict
service_api_key_dict = service_api_key_instance.to_dict()
# create an instance of ServiceAPIKey from a dict
service_api_key_from_dict = ServiceAPIKey.from_dict(service_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


