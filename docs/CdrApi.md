# openapi_client.CdrApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_cdr_cdr_id_get**](CdrApi.md#v1_account_account_id_cdr_cdr_id_get) | **GET** /v1/account/{accountID}/cdr/{cdrID} | 
[**v1_account_account_id_cdr_get**](CdrApi.md#v1_account_account_id_cdr_get) | **GET** /v1/account/{accountID}/cdr | 


# **v1_account_account_id_cdr_cdr_id_get**
> ServiceDocsCdrGetSingle v1_account_account_id_cdr_cdr_id_get(account_id, cdr_id)

Retrieve the details of a single CDR record from an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_cdr_get_single import ServiceDocsCdrGetSingle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CdrApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    cdr_id = 'cdr_id_example' # str | CDR ID, string

    try:
        api_response = api_instance.v1_account_account_id_cdr_cdr_id_get(account_id, cdr_id)
        print("The response of CdrApi->v1_account_account_id_cdr_cdr_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CdrApi->v1_account_account_id_cdr_cdr_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **cdr_id** | **str**| CDR ID, string | 

### Return type

[**ServiceDocsCdrGetSingle**](ServiceDocsCdrGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_account_id_cdr_get**
> ServiceDocsCdrGetAll v1_account_account_id_cdr_get(account_id, page_size, start_key, created_from, created_to)

Retrieve a list of CDRs in a specific account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_cdr_get_all import ServiceDocsCdrGetAll
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CdrApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    page_size = 'page_size_example' # str | Page size (Maximum number of results to display per page)
    start_key = 'start_key_example' # str | Start key (Starting offset for displaying results)
    created_from = 'created_from_example' # str | For displaying records which are created on or after this timestamp (Supported timestamp formats: iso 8601, unix time in seconds or milliseconds or microseconds or nanoseconds)
    created_to = 'created_to_example' # str | For displaying records which are created on or before this timestamp (Supported timestamp formats: iso 8601, unix time in seconds or milliseconds or microseconds or nanoseconds)

    try:
        api_response = api_instance.v1_account_account_id_cdr_get(account_id, page_size, start_key, created_from, created_to)
        print("The response of CdrApi->v1_account_account_id_cdr_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CdrApi->v1_account_account_id_cdr_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **page_size** | **str**| Page size (Maximum number of results to display per page) | 
 **start_key** | **str**| Start key (Starting offset for displaying results) | 
 **created_from** | **str**| For displaying records which are created on or after this timestamp (Supported timestamp formats: iso 8601, unix time in seconds or milliseconds or microseconds or nanoseconds) | 
 **created_to** | **str**| For displaying records which are created on or before this timestamp (Supported timestamp formats: iso 8601, unix time in seconds or milliseconds or microseconds or nanoseconds) | 

### Return type

[**ServiceDocsCdrGetAll**](ServiceDocsCdrGetAll.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

