# ServiceDocsAccountAPIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceAPIKey**](ServiceAPIKey.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_account_api_key import ServiceDocsAccountAPIKey

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsAccountAPIKey from a JSON string
service_docs_account_api_key_instance = ServiceDocsAccountAPIKey.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsAccountAPIKey.to_json())

# convert the object into a dict
service_docs_account_api_key_dict = service_docs_account_api_key_instance.to_dict()
# create an instance of ServiceDocsAccountAPIKey from a dict
service_docs_account_api_key_from_dict = ServiceDocsAccountAPIKey.from_dict(service_docs_account_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


