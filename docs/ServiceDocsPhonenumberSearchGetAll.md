# ServiceDocsPhonenumberSearchGetAll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServicePhoneNumberSearchOutput]**](ServicePhoneNumberSearchOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_phonenumber_search_get_all import ServiceDocsPhonenumberSearchGetAll

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsPhonenumberSearchGetAll from a JSON string
service_docs_phonenumber_search_get_all_instance = ServiceDocsPhonenumberSearchGetAll.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsPhonenumberSearchGetAll.to_json())

# convert the object into a dict
service_docs_phonenumber_search_get_all_dict = service_docs_phonenumber_search_get_all_instance.to_dict()
# create an instance of ServiceDocsPhonenumberSearchGetAll from a dict
service_docs_phonenumber_search_get_all_from_dict = ServiceDocsPhonenumberSearchGetAll.from_dict(service_docs_phonenumber_search_get_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


