# ProvisioningDocsDocsBrandOutputSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelsBrand**](ModelsBrand.md) |  | [optional] 
**request_id** | **str** | Unique id for each request | [optional] 
**status_code** | **int** | HTTP response status code | [optional] 

## Example

```python
from openapi_client.models.provisioning_docs_docs_brand_output_single import ProvisioningDocsDocsBrandOutputSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningDocsDocsBrandOutputSingle from a JSON string
provisioning_docs_docs_brand_output_single_instance = ProvisioningDocsDocsBrandOutputSingle.from_json(json)
# print the JSON string representation of the object
print(ProvisioningDocsDocsBrandOutputSingle.to_json())

# convert the object into a dict
provisioning_docs_docs_brand_output_single_dict = provisioning_docs_docs_brand_output_single_instance.to_dict()
# create an instance of ProvisioningDocsDocsBrandOutputSingle from a dict
provisioning_docs_docs_brand_output_single_from_dict = ProvisioningDocsDocsBrandOutputSingle.from_dict(provisioning_docs_docs_brand_output_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


