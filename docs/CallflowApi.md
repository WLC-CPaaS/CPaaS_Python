# openapi_client.CallflowApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_callflow_callflow_id_delete**](CallflowApi.md#v1_account_account_id_callflow_callflow_id_delete) | **DELETE** /v1/account/{accountID}/callflow/{callflowID} | Delete Call Group
[**v1_account_account_id_callflow_callflow_id_get**](CallflowApi.md#v1_account_account_id_callflow_callflow_id_get) | **GET** /v1/account/{accountID}/callflow/{callflowID} | Get Call Group Details
[**v1_account_account_id_callflow_callflow_id_put**](CallflowApi.md#v1_account_account_id_callflow_callflow_id_put) | **PUT** /v1/account/{accountID}/callflow/{callflowID} | Update Call Group
[**v1_account_account_id_callflow_get**](CallflowApi.md#v1_account_account_id_callflow_get) | **GET** /v1/account/{accountID}/callflow | Get Callflow List
[**v1_account_account_id_callflow_post**](CallflowApi.md#v1_account_account_id_callflow_post) | **POST** /v1/account/{accountID}/callflow | Create Call Group


# **v1_account_account_id_callflow_callflow_id_delete**
> ServiceDocsCallflowGetSingle v1_account_account_id_callflow_callflow_id_delete(account_id, callflow_id)

Delete Call Group

Delete a callflow in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_callflow_get_single import ServiceDocsCallflowGetSingle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    callflow_id = 'callflow_id_example' # str | callflow ID, 32 alpha numeric

    try:
        # Delete Call Group
        api_response = api_instance.v1_account_account_id_callflow_callflow_id_delete(account_id, callflow_id)
        print("The response of CallflowApi->v1_account_account_id_callflow_callflow_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallflowApi->v1_account_account_id_callflow_callflow_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **callflow_id** | **str**| callflow ID, 32 alpha numeric | 

### Return type

[**ServiceDocsCallflowGetSingle**](ServiceDocsCallflowGetSingle.md)

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

# **v1_account_account_id_callflow_callflow_id_get**
> ServiceDocsCallflowGetSingle v1_account_account_id_callflow_callflow_id_get(account_id, callflow_id)

Get Call Group Details

Get the details for a single callflow in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_callflow_get_single import ServiceDocsCallflowGetSingle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    callflow_id = 'callflow_id_example' # str | Callflow ID, 32 alpha numeric

    try:
        # Get Call Group Details
        api_response = api_instance.v1_account_account_id_callflow_callflow_id_get(account_id, callflow_id)
        print("The response of CallflowApi->v1_account_account_id_callflow_callflow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallflowApi->v1_account_account_id_callflow_callflow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **callflow_id** | **str**| Callflow ID, 32 alpha numeric | 

### Return type

[**ServiceDocsCallflowGetSingle**](ServiceDocsCallflowGetSingle.md)

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

# **v1_account_account_id_callflow_callflow_id_put**
> ServiceDocsCallflowGetSingle v1_account_account_id_callflow_callflow_id_put(account_id, callflow_id, req_body)

Update Call Group

Update the details for a single callflow in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_callflow_add_edit_data import ServiceCallflowAddEditData
from openapi_client.models.service_docs_callflow_get_single import ServiceDocsCallflowGetSingle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    callflow_id = 'callflow_id_example' # str | Callflow ID, 32 alpha numeric
    req_body = openapi_client.ServiceCallflowAddEditData() # ServiceCallflowAddEditData | payload fields

    try:
        # Update Call Group
        api_response = api_instance.v1_account_account_id_callflow_callflow_id_put(account_id, callflow_id, req_body)
        print("The response of CallflowApi->v1_account_account_id_callflow_callflow_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallflowApi->v1_account_account_id_callflow_callflow_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **callflow_id** | **str**| Callflow ID, 32 alpha numeric | 
 **req_body** | [**ServiceCallflowAddEditData**](ServiceCallflowAddEditData.md)| payload fields | 

### Return type

[**ServiceDocsCallflowGetSingle**](ServiceDocsCallflowGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_account_id_callflow_get**
> ServiceDocsCallflowGetAll v1_account_account_id_callflow_get(account_id, start_key=start_key, page_size=page_size)

Get Callflow List

Permit a user to view the callflow details in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_callflow_get_all import ServiceDocsCallflowGetAll
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Callflow List
        api_response = api_instance.v1_account_account_id_callflow_get(account_id, start_key=start_key, page_size=page_size)
        print("The response of CallflowApi->v1_account_account_id_callflow_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallflowApi->v1_account_account_id_callflow_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsCallflowGetAll**](ServiceDocsCallflowGetAll.md)

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

# **v1_account_account_id_callflow_post**
> ServiceDocsCallflowGetSingle v1_account_account_id_callflow_post(account_id, request)

Create Call Group

Create instructions for routing a call to a user or system.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_callflow_add_edit_data import ServiceCallflowAddEditData
from openapi_client.models.service_docs_callflow_get_single import ServiceDocsCallflowGetSingle
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://API_HOSTNAME
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://API_HOSTNAME"
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
    api_instance = openapi_client.CallflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha-numeric
    request = openapi_client.ServiceCallflowAddEditData() # ServiceCallflowAddEditData | Call flow configuration

    try:
        # Create Call Group
        api_response = api_instance.v1_account_account_id_callflow_post(account_id, request)
        print("The response of CallflowApi->v1_account_account_id_callflow_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallflowApi->v1_account_account_id_callflow_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha-numeric | 
 **request** | [**ServiceCallflowAddEditData**](ServiceCallflowAddEditData.md)| Call flow configuration | 

### Return type

[**ServiceDocsCallflowGetSingle**](ServiceDocsCallflowGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

