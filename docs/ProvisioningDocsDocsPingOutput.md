# ProvisioningDocsDocsPingOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProvisioningDocsDocsPingOutputData**](ProvisioningDocsDocsPingOutputData.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.provisioning_docs_docs_ping_output import ProvisioningDocsDocsPingOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningDocsDocsPingOutput from a JSON string
provisioning_docs_docs_ping_output_instance = ProvisioningDocsDocsPingOutput.from_json(json)
# print the JSON string representation of the object
print(ProvisioningDocsDocsPingOutput.to_json())

# convert the object into a dict
provisioning_docs_docs_ping_output_dict = provisioning_docs_docs_ping_output_instance.to_dict()
# create an instance of ProvisioningDocsDocsPingOutput from a dict
provisioning_docs_docs_ping_output_from_dict = ProvisioningDocsDocsPingOutput.from_dict(provisioning_docs_docs_ping_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


