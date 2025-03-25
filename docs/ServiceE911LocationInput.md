# ServiceE911LocationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_1** | **str** |  | 
**address_2** | **str** |  | [optional] 
**community** | **str** |  | 
**plus_four** | **str** |  | [optional] 
**postal_code** | **str** |  | 
**state** | **str** |  | 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_e911_location_input import ServiceE911LocationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911LocationInput from a JSON string
service_e911_location_input_instance = ServiceE911LocationInput.from_json(json)
# print the JSON string representation of the object
print(ServiceE911LocationInput.to_json())

# convert the object into a dict
service_e911_location_input_dict = service_e911_location_input_instance.to_dict()
# create an instance of ServiceE911LocationInput from a dict
service_e911_location_input_from_dict = ServiceE911LocationInput.from_dict(service_e911_location_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


