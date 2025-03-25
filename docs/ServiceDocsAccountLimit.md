# ServiceDocsAccountLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceAccountLimitOutput**](ServiceAccountLimitOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_account_limit import ServiceDocsAccountLimit

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsAccountLimit from a JSON string
service_docs_account_limit_instance = ServiceDocsAccountLimit.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsAccountLimit.to_json())

# convert the object into a dict
service_docs_account_limit_dict = service_docs_account_limit_instance.to_dict()
# create an instance of ServiceDocsAccountLimit from a dict
service_docs_account_limit_from_dict = ServiceDocsAccountLimit.from_dict(service_docs_account_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


