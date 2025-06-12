# openapi_client.ProvisionApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_provision_filename_get**](ProvisionApi.md#v1_account_account_id_provision_filename_get) | **GET** /v1/account/{accountID}/provision/{filename} | 


# **v1_account_account_id_provision_filename_get**
> bytearray v1_account_account_id_provision_filename_get(account_id, filename)

Retrieve the configuration details (e.g., settings and parameters) for a device.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProvisionApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    filename = 'filename_example' # str | Name of config file

    try:
        api_response = api_instance.v1_account_account_id_provision_filename_get(account_id, filename)
        print("The response of ProvisionApi->v1_account_account_id_provision_filename_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisionApi->v1_account_account_id_provision_filename_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **filename** | **str**| Name of config file | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

