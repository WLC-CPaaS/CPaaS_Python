# ServiceE911LegacyDataOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**house_number** | **str** |  | [optional] 
**predirectional** | **str** |  | [optional] 
**street_name** | **str** |  | [optional] 
**suite** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_e911_legacy_data_output import ServiceE911LegacyDataOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911LegacyDataOutput from a JSON string
service_e911_legacy_data_output_instance = ServiceE911LegacyDataOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceE911LegacyDataOutput.to_json())

# convert the object into a dict
service_e911_legacy_data_output_dict = service_e911_legacy_data_output_instance.to_dict()
# create an instance of ServiceE911LegacyDataOutput from a dict
service_e911_legacy_data_output_from_dict = ServiceE911LegacyDataOutput.from_dict(service_e911_legacy_data_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


