# ServiceE911LocationURILegacyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**house_number** | **str** |  | [optional] 
**predirectional** | **str** |  | [optional] 
**street_name** | **str** |  | [optional] 
**suite** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_e911_location_uri_legacy_data import ServiceE911LocationURILegacyData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911LocationURILegacyData from a JSON string
service_e911_location_uri_legacy_data_instance = ServiceE911LocationURILegacyData.from_json(json)
# print the JSON string representation of the object
print(ServiceE911LocationURILegacyData.to_json())

# convert the object into a dict
service_e911_location_uri_legacy_data_dict = service_e911_location_uri_legacy_data_instance.to_dict()
# create an instance of ServiceE911LocationURILegacyData from a dict
service_e911_location_uri_legacy_data_from_dict = ServiceE911LocationURILegacyData.from_dict(service_e911_location_uri_legacy_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


