# ServiceCampaignImportOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** |  | [optional] 
**created_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**message_class** | **str** |  | [optional] 
**mno_status_list** | [**List[ServiceCampaignImportOutputMnoStatusListInner]**](ServiceCampaignImportOutputMnoStatusListInner.md) |  | [optional] 
**secondary_dca_sharing_status** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_campaign_import_output import ServiceCampaignImportOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCampaignImportOutput from a JSON string
service_campaign_import_output_instance = ServiceCampaignImportOutput.from_json(json)
# print the JSON string representation of the object
print(ServiceCampaignImportOutput.to_json())

# convert the object into a dict
service_campaign_import_output_dict = service_campaign_import_output_instance.to_dict()
# create an instance of ServiceCampaignImportOutput from a dict
service_campaign_import_output_from_dict = ServiceCampaignImportOutput.from_dict(service_campaign_import_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


