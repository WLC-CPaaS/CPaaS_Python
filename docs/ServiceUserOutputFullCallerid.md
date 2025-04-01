# ServiceUserOutputFullCallerid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emergency** | [**ServiceUserOutputFullCalleridEmergency**](ServiceUserOutputFullCalleridEmergency.md) |  | [optional] 
**external** | [**ServiceUserOutputFullCalleridExternal**](ServiceUserOutputFullCalleridExternal.md) |  | [optional] 
**internal** | [**ServiceUserOutputFullCalleridInternal**](ServiceUserOutputFullCalleridInternal.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_user_output_full_callerid import ServiceUserOutputFullCallerid

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUserOutputFullCallerid from a JSON string
service_user_output_full_callerid_instance = ServiceUserOutputFullCallerid.from_json(json)
# print the JSON string representation of the object
print(ServiceUserOutputFullCallerid.to_json())

# convert the object into a dict
service_user_output_full_callerid_dict = service_user_output_full_callerid_instance.to_dict()
# create an instance of ServiceUserOutputFullCallerid from a dict
service_user_output_full_callerid_from_dict = ServiceUserOutputFullCallerid.from_dict(service_user_output_full_callerid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


