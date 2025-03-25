# ServiceAccountLimitOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound_trunks** | **int** |  | [optional] 
**outbound_trunks** | **int** |  | [optional] 
**twoway_trunks** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.service_account_limit_output import ServiceAccountLimitOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountLimitOutput from a JSON string
service_account_limit_output_instance = ServiceAccountLimitOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountLimitOutput.to_json())

# convert the object into a dict
service_account_limit_output_dict = service_account_limit_output_instance.to_dict()
# create an instance of ServiceAccountLimitOutput from a dict
service_account_limit_output_from_dict = ServiceAccountLimitOutput.from_dict(service_account_limit_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


