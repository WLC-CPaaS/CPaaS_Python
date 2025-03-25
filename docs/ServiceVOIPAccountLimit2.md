# ServiceVOIPAccountLimit2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound_trunks** | **int** |  | 
**outbound_trunks** | **int** |  | 
**twoway_trunks** | **int** |  | 

## Example

```python
from openapi_client.models.service_voip_account_limit2 import ServiceVOIPAccountLimit2

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPAccountLimit2 from a JSON string
service_voip_account_limit2_instance = ServiceVOIPAccountLimit2.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPAccountLimit2.to_json())

# convert the object into a dict
service_voip_account_limit2_dict = service_voip_account_limit2_instance.to_dict()
# create an instance of ServiceVOIPAccountLimit2 from a dict
service_voip_account_limit2_from_dict = ServiceVOIPAccountLimit2.from_dict(service_voip_account_limit2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


