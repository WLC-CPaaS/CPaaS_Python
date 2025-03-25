# ServiceE911LocationOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_time** | **str** |  | [optional] 
**address_1** | **str** |  | [optional] 
**address_2** | **str** |  | [optional] 
**caller_name** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**community** | **str** |  | [optional] 
**customer_order_id** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**legacy_data** | [**ServiceE911LegacyDataOutput**](ServiceE911LegacyDataOutput.md) |  | [optional] 
**location_id** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**plus_four** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**status** | [**ServiceE911StatusOutput**](ServiceE911StatusOutput.md) |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_e911_location_output import ServiceE911LocationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911LocationOutput from a JSON string
service_e911_location_output_instance = ServiceE911LocationOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceE911LocationOutput.to_json())

# convert the object into a dict
service_e911_location_output_dict = service_e911_location_output_instance.to_dict()
# create an instance of ServiceE911LocationOutput from a dict
service_e911_location_output_from_dict = ServiceE911LocationOutput.from_dict(service_e911_location_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


