# ServiceVOIPAccountOutputFullCallerid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emergency** | [**ServiceAccountOutputFullCalleridEmergency**](ServiceAccountOutputFullCalleridEmergency.md) |  | [optional] 
**external** | [**ServiceAccountOutputFullCalleridExternal**](ServiceAccountOutputFullCalleridExternal.md) |  | [optional] 
**internal** | [**ServiceAccountOutputFullCalleridInternal**](ServiceAccountOutputFullCalleridInternal.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_voip_account_output_full_callerid import ServiceVOIPAccountOutputFullCallerid

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVOIPAccountOutputFullCallerid from a JSON string
service_voip_account_output_full_callerid_instance = ServiceVOIPAccountOutputFullCallerid.from_json(json)
# print the JSON string representation of the object
print(ServiceVOIPAccountOutputFullCallerid.to_json())

# convert the object into a dict
service_voip_account_output_full_callerid_dict = service_voip_account_output_full_callerid_instance.to_dict()
# create an instance of ServiceVOIPAccountOutputFullCallerid from a dict
service_voip_account_output_full_callerid_from_dict = ServiceVOIPAccountOutputFullCallerid.from_dict(service_voip_account_output_full_callerid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


