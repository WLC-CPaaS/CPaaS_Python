# ServiceDocsCampaignImportOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceCampaignImportOutput**](ServiceCampaignImportOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_campaign_import_output import ServiceDocsCampaignImportOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsCampaignImportOutput from a JSON string
service_docs_campaign_import_output_instance = ServiceDocsCampaignImportOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsCampaignImportOutput.to_json())

# convert the object into a dict
service_docs_campaign_import_output_dict = service_docs_campaign_import_output_instance.to_dict()
# create an instance of ServiceDocsCampaignImportOutput from a dict
service_docs_campaign_import_output_from_dict = ServiceDocsCampaignImportOutput.from_dict(service_docs_campaign_import_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


