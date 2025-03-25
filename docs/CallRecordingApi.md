# openapi_client.CallRecordingApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_recording_get**](CallRecordingApi.md#v1_account_account_id_recording_get) | **GET** /v1/account/{accountID}/recording | Get Account Call Recording
[**v1_account_account_id_recording_recording_id_delete**](CallRecordingApi.md#v1_account_account_id_recording_recording_id_delete) | **DELETE** /v1/account/{accountID}/recording/{recordingID} | Delete Call Recording
[**v1_account_account_id_recording_recording_id_get**](CallRecordingApi.md#v1_account_account_id_recording_recording_id_get) | **GET** /v1/account/{accountID}/recording/{recordingID} | Get Call Recording Details
[**v1_account_account_id_user_user_id_recording_get**](CallRecordingApi.md#v1_account_account_id_user_user_id_recording_get) | **GET** /v1/account/{accountID}/user/{userID}/recording | Get User Call Recording


# **v1_account_account_id_recording_get**
> ServiceDocsCallRecordingGetAll v1_account_account_id_recording_get(account_id)

Get Account Call Recording

Obtain a list of the call recordings within an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_recording_get_all import ServiceDocsCallRecordingGetAll
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
    api_instance = openapi_client.CallRecordingApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Account Call Recording
        api_response = api_instance.v1_account_account_id_recording_get(account_id)
        print("The response of CallRecordingApi->v1_account_account_id_recording_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallRecordingApi->v1_account_account_id_recording_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsCallRecordingGetAll**](ServiceDocsCallRecordingGetAll.md)

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

# **v1_account_account_id_recording_recording_id_delete**
> ServiceDocsCallRecordingGetSingle v1_account_account_id_recording_recording_id_delete(account_id, recording_id)

Delete Call Recording

Delete a single call recording from an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_recording_get_single import ServiceDocsCallRecordingGetSingle
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
    api_instance = openapi_client.CallRecordingApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    recording_id = 'recording_id_example' # str | Recording ID, 39 (yyyymm-<32 id>)

    try:
        # Delete Call Recording
        api_response = api_instance.v1_account_account_id_recording_recording_id_delete(account_id, recording_id)
        print("The response of CallRecordingApi->v1_account_account_id_recording_recording_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallRecordingApi->v1_account_account_id_recording_recording_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **recording_id** | **str**| Recording ID, 39 (yyyymm-&lt;32 id&gt;) | 

### Return type

[**ServiceDocsCallRecordingGetSingle**](ServiceDocsCallRecordingGetSingle.md)

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

# **v1_account_account_id_recording_recording_id_get**
> ServiceDocsCallRecordingGetSingle v1_account_account_id_recording_recording_id_get(account_id, recording_id)

Get Call Recording Details

Access details for each recorded call in an account (e.g., duration, names and numbers of call participants, etc.).

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_recording_get_single import ServiceDocsCallRecordingGetSingle
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
    api_instance = openapi_client.CallRecordingApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    recording_id = 'recording_id_example' # str | Recording ID, 39 (yyyymm-<32 id>)

    try:
        # Get Call Recording Details
        api_response = api_instance.v1_account_account_id_recording_recording_id_get(account_id, recording_id)
        print("The response of CallRecordingApi->v1_account_account_id_recording_recording_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallRecordingApi->v1_account_account_id_recording_recording_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **recording_id** | **str**| Recording ID, 39 (yyyymm-&lt;32 id&gt;) | 

### Return type

[**ServiceDocsCallRecordingGetSingle**](ServiceDocsCallRecordingGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, audio/mp3, audio/mpeg, audio/mpeg3, audio/x-wav, audio/wav

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_account_id_user_user_id_recording_get**
> ServiceDocsCallRecordingGetAll v1_account_account_id_user_user_id_recording_get(account_id, user_id)

Get User Call Recording

Retrieve a list of call recordings for a user within an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_call_recording_get_all import ServiceDocsCallRecordingGetAll
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
    api_instance = openapi_client.CallRecordingApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    user_id = 'user_id_example' # str | User ID, 32 alpha numeric

    try:
        # Get User Call Recording
        api_response = api_instance.v1_account_account_id_user_user_id_recording_get(account_id, user_id)
        print("The response of CallRecordingApi->v1_account_account_id_user_user_id_recording_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallRecordingApi->v1_account_account_id_user_user_id_recording_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **user_id** | **str**| User ID, 32 alpha numeric | 

### Return type

[**ServiceDocsCallRecordingGetAll**](ServiceDocsCallRecordingGetAll.md)

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

