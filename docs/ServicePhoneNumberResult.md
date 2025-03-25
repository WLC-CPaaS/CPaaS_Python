# ServicePhoneNumberResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**phonenumber** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_phone_number_result import ServicePhoneNumberResult

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePhoneNumberResult from a JSON string
service_phone_number_result_instance = ServicePhoneNumberResult.from_json(json)
# print the JSON string representation of the object
print(ServicePhoneNumberResult.to_json())

# convert the object into a dict
service_phone_number_result_dict = service_phone_number_result_instance.to_dict()
# create an instance of ServicePhoneNumberResult from a dict
service_phone_number_result_from_dict = ServicePhoneNumberResult.from_dict(service_phone_number_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


