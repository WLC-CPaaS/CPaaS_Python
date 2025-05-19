# ModelsVOIPAccountOutputFullCallerid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emergency** | [**ModelsAccountOutputFullCalleridEmergency**](ModelsAccountOutputFullCalleridEmergency.md) |  | [optional] 
**external** | [**ModelsAccountOutputFullCalleridExternal**](ModelsAccountOutputFullCalleridExternal.md) |  | [optional] 
**internal** | [**ModelsAccountOutputFullCalleridInternal**](ModelsAccountOutputFullCalleridInternal.md) |  | [optional] 

## Example

```python
from openapi_client.models.models_voip_account_output_full_callerid import ModelsVOIPAccountOutputFullCallerid

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsVOIPAccountOutputFullCallerid from a JSON string
models_voip_account_output_full_callerid_instance = ModelsVOIPAccountOutputFullCallerid.from_json(json)
# print the JSON string representation of the object
print(ModelsVOIPAccountOutputFullCallerid.to_json())

# convert the object into a dict
models_voip_account_output_full_callerid_dict = models_voip_account_output_full_callerid_instance.to_dict()
# create an instance of ModelsVOIPAccountOutputFullCallerid from a dict
models_voip_account_output_full_callerid_from_dict = ModelsVOIPAccountOutputFullCallerid.from_dict(models_voip_account_output_full_callerid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


