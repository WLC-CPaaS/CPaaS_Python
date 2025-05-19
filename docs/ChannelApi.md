# openapi_client.ChannelApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_channel_channel_id_get**](ChannelApi.md#v1_account_account_id_channel_channel_id_get) | **GET** /v1/account/{accountID}/channel/{channelID} | Get Channel Details
[**v1_account_account_id_channel_channel_id_post**](ChannelApi.md#v1_account_account_id_channel_channel_id_post) | **POST** /v1/account/{accountID}/channel/{channelID} | Associate Action to Channel
[**v1_account_account_id_channel_channel_id_put**](ChannelApi.md#v1_account_account_id_channel_channel_id_put) | **PUT** /v1/account/{accountID}/channel/{channelID} | Associate Metaflow to Channel
[**v1_account_account_id_channel_get**](ChannelApi.md#v1_account_account_id_channel_get) | **GET** /v1/account/{accountID}/channel | Get Account Channel List
[**v1_account_account_id_device_device_id_channel_get**](ChannelApi.md#v1_account_account_id_device_device_id_channel_get) | **GET** /v1/account/{accountID}/device/{deviceID}/channel | Get Device Channel List
[**v1_account_account_id_user_user_id_channel_get**](ChannelApi.md#v1_account_account_id_user_user_id_channel_get) | **GET** /v1/account/{accountID}/user/{userID}/channel | Get User Channel List


# **v1_account_account_id_channel_channel_id_get**
> ServiceDocsChannelGetSingle v1_account_account_id_channel_channel_id_get(account_id, channel_id)

Get Channel Details

Access details about each channel in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_channel_get_single import ServiceDocsChannelGetSingle
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
    api_instance = openapi_client.ChannelApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    channel_id = 'channel_id_example' # str | Channel ID

    try:
        # Get Channel Details
        api_response = api_instance.v1_account_account_id_channel_channel_id_get(account_id, channel_id)
        print("The response of ChannelApi->v1_account_account_id_channel_channel_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelApi->v1_account_account_id_channel_channel_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **channel_id** | **str**| Channel ID | 

### Return type

[**ServiceDocsChannelGetSingle**](ServiceDocsChannelGetSingle.md)

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

# **v1_account_account_id_channel_channel_id_post**
> ServiceAPIResponse v1_account_account_id_channel_channel_id_post(account_id, channel_id, req_body)

Associate Action to Channel

Link an action, such as transfer or hangup to a channel.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response import ServiceAPIResponse
from openapi_client.models.service_voip_channel_run_action_data import ServiceVOIPChannelRunActionData
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
    api_instance = openapi_client.ChannelApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    channel_id = 'channel_id_example' # str | Channel ID
    req_body = openapi_client.ServiceVOIPChannelRunActionData() # ServiceVOIPChannelRunActionData | payload fields

    try:
        # Associate Action to Channel
        api_response = api_instance.v1_account_account_id_channel_channel_id_post(account_id, channel_id, req_body)
        print("The response of ChannelApi->v1_account_account_id_channel_channel_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelApi->v1_account_account_id_channel_channel_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **channel_id** | **str**| Channel ID | 
 **req_body** | [**ServiceVOIPChannelRunActionData**](ServiceVOIPChannelRunActionData.md)| payload fields | 

### Return type

[**ServiceAPIResponse**](ServiceAPIResponse.md)

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

# **v1_account_account_id_channel_channel_id_put**
> ServiceAPIResponse v1_account_account_id_channel_channel_id_put(account_id, channel_id, req_body)

Associate Metaflow to Channel

Link a metaflow to an active channel.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response import ServiceAPIResponse
from openapi_client.models.service_voip_channel_run_metaflow_data import ServiceVOIPChannelRunMetaflowData
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
    api_instance = openapi_client.ChannelApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    channel_id = 'channel_id_example' # str | Channel ID
    req_body = openapi_client.ServiceVOIPChannelRunMetaflowData() # ServiceVOIPChannelRunMetaflowData | payload fields

    try:
        # Associate Metaflow to Channel
        api_response = api_instance.v1_account_account_id_channel_channel_id_put(account_id, channel_id, req_body)
        print("The response of ChannelApi->v1_account_account_id_channel_channel_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelApi->v1_account_account_id_channel_channel_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **channel_id** | **str**| Channel ID | 
 **req_body** | [**ServiceVOIPChannelRunMetaflowData**](ServiceVOIPChannelRunMetaflowData.md)| payload fields | 

### Return type

[**ServiceAPIResponse**](ServiceAPIResponse.md)

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

# **v1_account_account_id_channel_get**
> ServiceDocsChannelGetAll v1_account_account_id_channel_get(account_id)

Get Account Channel List

Get a list of active channels for an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_channel_get_all import ServiceDocsChannelGetAll
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
    api_instance = openapi_client.ChannelApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Account Channel List
        api_response = api_instance.v1_account_account_id_channel_get(account_id)
        print("The response of ChannelApi->v1_account_account_id_channel_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelApi->v1_account_account_id_channel_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsChannelGetAll**](ServiceDocsChannelGetAll.md)

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

# **v1_account_account_id_device_device_id_channel_get**
> ServiceDocsChannelGetAll v1_account_account_id_device_device_id_channel_get(account_id, device_id)

Get Device Channel List

Get the list of active channels for a device.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_channel_get_all import ServiceDocsChannelGetAll
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
    api_instance = openapi_client.ChannelApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    device_id = 'device_id_example' # str | Device ID, 32 alpha numeric

    try:
        # Get Device Channel List
        api_response = api_instance.v1_account_account_id_device_device_id_channel_get(account_id, device_id)
        print("The response of ChannelApi->v1_account_account_id_device_device_id_channel_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelApi->v1_account_account_id_device_device_id_channel_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **device_id** | **str**| Device ID, 32 alpha numeric | 

### Return type

[**ServiceDocsChannelGetAll**](ServiceDocsChannelGetAll.md)

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

# **v1_account_account_id_user_user_id_channel_get**
> ServiceDocsChannelGetAll v1_account_account_id_user_user_id_channel_get(account_id, user_id)

Get User Channel List

Get the list of active channels for a user.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_channel_get_all import ServiceDocsChannelGetAll
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
    api_instance = openapi_client.ChannelApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    user_id = 'user_id_example' # str | User ID, 32 alpha numeric

    try:
        # Get User Channel List
        api_response = api_instance.v1_account_account_id_user_user_id_channel_get(account_id, user_id)
        print("The response of ChannelApi->v1_account_account_id_user_user_id_channel_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelApi->v1_account_account_id_user_user_id_channel_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **user_id** | **str**| User ID, 32 alpha numeric | 

### Return type

[**ServiceDocsChannelGetAll**](ServiceDocsChannelGetAll.md)

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

