# ProvisioningDocsDocsConfigFileOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**next_start_key** | **str** | List Pagination: Used to get the next page of results. Will not exist if this is the last page. | [optional] 
**page_size** | **int** | List Pagination: The number of results returned in this page | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**start_key** | **str** | List Pagination: Code for paged results | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.provisioning_docs_docs_config_file_output import ProvisioningDocsDocsConfigFileOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningDocsDocsConfigFileOutput from a JSON string
provisioning_docs_docs_config_file_output_instance = ProvisioningDocsDocsConfigFileOutput.from_json(json)
# print the JSON string representation of the object
print(ProvisioningDocsDocsConfigFileOutput.to_json())

# convert the object into a dict
provisioning_docs_docs_config_file_output_dict = provisioning_docs_docs_config_file_output_instance.to_dict()
# create an instance of ProvisioningDocsDocsConfigFileOutput from a dict
provisioning_docs_docs_config_file_output_from_dict = ProvisioningDocsDocsConfigFileOutput.from_dict(provisioning_docs_docs_config_file_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


