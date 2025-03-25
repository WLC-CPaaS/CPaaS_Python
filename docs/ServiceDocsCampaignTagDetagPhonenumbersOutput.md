# ServiceDocsCampaignTagDetagPhonenumbersOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceCampaignTagDetagPhonenumbersOutput**](ServiceCampaignTagDetagPhonenumbersOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_campaign_tag_detag_phonenumbers_output import ServiceDocsCampaignTagDetagPhonenumbersOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsCampaignTagDetagPhonenumbersOutput from a JSON string
service_docs_campaign_tag_detag_phonenumbers_output_instance = ServiceDocsCampaignTagDetagPhonenumbersOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsCampaignTagDetagPhonenumbersOutput.to_json())

# convert the object into a dict
service_docs_campaign_tag_detag_phonenumbers_output_dict = service_docs_campaign_tag_detag_phonenumbers_output_instance.to_dict()
# create an instance of ServiceDocsCampaignTagDetagPhonenumbersOutput from a dict
service_docs_campaign_tag_detag_phonenumbers_output_from_dict = ServiceDocsCampaignTagDetagPhonenumbersOutput.from_dict(service_docs_campaign_tag_detag_phonenumbers_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


