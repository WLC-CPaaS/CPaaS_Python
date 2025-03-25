# ServiceDocsCampaignImportedGetAllOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceCampaignImportOutput]**](ServiceCampaignImportOutput.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.service_docs_campaign_imported_get_all_output import ServiceDocsCampaignImportedGetAllOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDocsCampaignImportedGetAllOutput from a JSON string
service_docs_campaign_imported_get_all_output_instance = ServiceDocsCampaignImportedGetAllOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceDocsCampaignImportedGetAllOutput.to_json())

# convert the object into a dict
service_docs_campaign_imported_get_all_output_dict = service_docs_campaign_imported_get_all_output_instance.to_dict()
# create an instance of ServiceDocsCampaignImportedGetAllOutput from a dict
service_docs_campaign_imported_get_all_output_from_dict = ServiceDocsCampaignImportedGetAllOutput.from_dict(service_docs_campaign_imported_get_all_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


