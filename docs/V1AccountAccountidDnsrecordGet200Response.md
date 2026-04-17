# V1AccountAccountidDnsrecordGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TypesResourceRecordSet**](TypesResourceRecordSet.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.v1_account_accountid_dnsrecord_get200_response import V1AccountAccountidDnsrecordGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AccountAccountidDnsrecordGet200Response from a JSON string
v1_account_accountid_dnsrecord_get200_response_instance = V1AccountAccountidDnsrecordGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1AccountAccountidDnsrecordGet200Response.to_json())

# convert the object into a dict
v1_account_accountid_dnsrecord_get200_response_dict = v1_account_accountid_dnsrecord_get200_response_instance.to_dict()
# create an instance of V1AccountAccountidDnsrecordGet200Response from a dict
v1_account_accountid_dnsrecord_get200_response_from_dict = V1AccountAccountidDnsrecordGet200Response.from_dict(v1_account_accountid_dnsrecord_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


