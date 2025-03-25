# openapi_client.PresenceApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_presence_extension_put**](PresenceApi.md#v1_account_account_id_presence_extension_put) | **PUT** /v1/account/{accountID}/presence/{extension} | Set/Reset Presence for Extension
[**v1_account_account_id_presence_get**](PresenceApi.md#v1_account_account_id_presence_get) | **GET** /v1/account/{accountID}/presence | Get Presence Details
[**v1_account_account_id_user_user_id_presence_put**](PresenceApi.md#v1_account_account_id_user_user_id_presence_put) | **PUT** /v1/account/{accountID}/user/{userID}/presence | Set/Reset Presence for User


# **v1_account_account_id_presence_extension_put**
> ServiceAPIResponse v1_account_account_id_presence_extension_put(account_id, extension, req_body)

Set/Reset Presence for Extension

Set or reset the presence status of an extension.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response import ServiceAPIResponse
from openapi_client.models.service_voip_presence_set_reset_edit_data import ServiceVOIPPresenceSetResetEditData
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
    api_instance = openapi_client.PresenceApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    extension = 'extension_example' # str | Extension
    req_body = openapi_client.ServiceVOIPPresenceSetResetEditData() # ServiceVOIPPresenceSetResetEditData | payload fields

    try:
        # Set/Reset Presence for Extension
        api_response = api_instance.v1_account_account_id_presence_extension_put(account_id, extension, req_body)
        print("The response of PresenceApi->v1_account_account_id_presence_extension_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PresenceApi->v1_account_account_id_presence_extension_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **extension** | **str**| Extension | 
 **req_body** | [**ServiceVOIPPresenceSetResetEditData**](ServiceVOIPPresenceSetResetEditData.md)| payload fields | 

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

# **v1_account_account_id_presence_get**
> ServiceDocsPresenceGet v1_account_account_id_presence_get(account_id)

Get Presence Details

Retrieve details of presence subscriptions in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_presence_get import ServiceDocsPresenceGet
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
    api_instance = openapi_client.PresenceApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Presence Details
        api_response = api_instance.v1_account_account_id_presence_get(account_id)
        print("The response of PresenceApi->v1_account_account_id_presence_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PresenceApi->v1_account_account_id_presence_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsPresenceGet**](ServiceDocsPresenceGet.md)

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

# **v1_account_account_id_user_user_id_presence_put**
> ServiceAPIResponse v1_account_account_id_user_user_id_presence_put(account_id, user_id, req_body)

Set/Reset Presence for User

Set or reset the presence status of a user within an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response import ServiceAPIResponse
from openapi_client.models.service_voip_presence_set_reset_edit_data import ServiceVOIPPresenceSetResetEditData
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
    api_instance = openapi_client.PresenceApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    user_id = 'user_id_example' # str | User ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPPresenceSetResetEditData() # ServiceVOIPPresenceSetResetEditData | payload fields

    try:
        # Set/Reset Presence for User
        api_response = api_instance.v1_account_account_id_user_user_id_presence_put(account_id, user_id, req_body)
        print("The response of PresenceApi->v1_account_account_id_user_user_id_presence_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PresenceApi->v1_account_account_id_user_user_id_presence_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **user_id** | **str**| User ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPPresenceSetResetEditData**](ServiceVOIPPresenceSetResetEditData.md)| payload fields | 

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

