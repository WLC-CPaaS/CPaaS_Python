# ServiceE911LocationURI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_time** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**caller_name** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**community** | **str** |  | [optional] 
**customer_order_id** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**legacy_data** | [**ServiceE911LocationURILegacyData**](ServiceE911LocationURILegacyData.md) |  | [optional] 
**location_id** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**plus_four** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**status** | [**ServiceE911LocationURIStatus**](ServiceE911LocationURIStatus.md) |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_e911_location_uri import ServiceE911LocationURI

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceE911LocationURI from a JSON string
service_e911_location_uri_instance = ServiceE911LocationURI.from_json(json)
# print the JSON string representation of the object
print(ServiceE911LocationURI.to_json())

# convert the object into a dict
service_e911_location_uri_dict = service_e911_location_uri_instance.to_dict()
# create an instance of ServiceE911LocationURI from a dict
service_e911_location_uri_from_dict = ServiceE911LocationURI.from_dict(service_e911_location_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


