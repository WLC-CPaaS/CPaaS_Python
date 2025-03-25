# ServiceCampaignPhoneNumberOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**telephone_numbers** | **List[str]** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.service_campaign_phone_number_output import ServiceCampaignPhoneNumberOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCampaignPhoneNumberOutput from a JSON string
service_campaign_phone_number_output_instance = ServiceCampaignPhoneNumberOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceCampaignPhoneNumberOutput.to_json())

# convert the object into a dict
service_campaign_phone_number_output_dict = service_campaign_phone_number_output_instance.to_dict()
# create an instance of ServiceCampaignPhoneNumberOutput from a dict
service_campaign_phone_number_output_from_dict = ServiceCampaignPhoneNumberOutput.from_dict(service_campaign_phone_number_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


