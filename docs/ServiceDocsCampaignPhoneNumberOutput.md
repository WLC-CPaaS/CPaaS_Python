# ServiceDocsCampaignPhoneNumberOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceCampaignPhoneNumberOutput**](ServiceCampaignPhoneNumberOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_campaign_phone_number_output import ServiceDocsCampaignPhoneNumberOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsCampaignPhoneNumberOutput from a JSON string
service_docs_campaign_phone_number_output_instance = ServiceDocsCampaignPhoneNumberOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsCampaignPhoneNumberOutput.to_json())

# convert the object into a dict
service_docs_campaign_phone_number_output_dict = service_docs_campaign_phone_number_output_instance.to_dict()
# create an instance of ServiceDocsCampaignPhoneNumberOutput from a dict
service_docs_campaign_phone_number_output_from_dict = ServiceDocsCampaignPhoneNumberOutput.from_dict(service_docs_campaign_phone_number_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


