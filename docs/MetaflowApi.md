# openapi_client.MetaflowApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_device_device_id_metaflow_delete**](MetaflowApi.md#v1_account_account_id_device_device_id_metaflow_delete) | **DELETE** /v1/account/{accountID}/device/{deviceID}/metaflow | Delete Device Metaflow
[**v1_account_account_id_device_device_id_metaflow_get**](MetaflowApi.md#v1_account_account_id_device_device_id_metaflow_get) | **GET** /v1/account/{accountID}/device/{deviceID}/metaflow | Get Device Metaflow List
[**v1_account_account_id_device_device_id_metaflow_post**](MetaflowApi.md#v1_account_account_id_device_device_id_metaflow_post) | **POST** /v1/account/{accountID}/device/{deviceID}/metaflow | Create Device Metaflow
[**v1_account_account_id_metaflow_delete**](MetaflowApi.md#v1_account_account_id_metaflow_delete) | **DELETE** /v1/account/{accountID}/metaflow | Delete Account Metaflow
[**v1_account_account_id_metaflow_get**](MetaflowApi.md#v1_account_account_id_metaflow_get) | **GET** /v1/account/{accountID}/metaflow | Get Account Metaflow List
[**v1_account_account_id_metaflow_post**](MetaflowApi.md#v1_account_account_id_metaflow_post) | **POST** /v1/account/{accountID}/metaflow | Create Account Metaflow
[**v1_account_account_id_user_user_id_metaflow_delete**](MetaflowApi.md#v1_account_account_id_user_user_id_metaflow_delete) | **DELETE** /v1/account/{accountID}/user/{userID}/metaflow | Delete User Metaflow
[**v1_account_account_id_user_user_id_metaflow_get**](MetaflowApi.md#v1_account_account_id_user_user_id_metaflow_get) | **GET** /v1/account/{accountID}/user/{userID}/metaflow | Get User Metaflow List
[**v1_account_account_id_user_user_id_metaflow_post**](MetaflowApi.md#v1_account_account_id_user_user_id_metaflow_post) | **POST** /v1/account/{accountID}/user/{userID}/metaflow | Create User Metaflow


# **v1_account_account_id_device_device_id_metaflow_delete**
> ServiceDocMetaflowGet v1_account_account_id_device_device_id_metaflow_delete(account_id, device_id)

Delete Device Metaflow

Delete all metaflows associated with a device.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet
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
    api_instance = openapi_client.MetaflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    device_id = 'device_id_example' # str | Device ID, 32 alpha numeric

    try:
        # Delete Device Metaflow
        api_response = api_instance.v1_account_account_id_device_device_id_metaflow_delete(account_id, device_id)
        print("The response of MetaflowApi->v1_account_account_id_device_device_id_metaflow_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaflowApi->v1_account_account_id_device_device_id_metaflow_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **device_id** | **str**| Device ID, 32 alpha numeric | 

### Return type

[**ServiceDocMetaflowGet**](ServiceDocMetaflowGet.md)

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

# **v1_account_account_id_device_device_id_metaflow_get**
> ServiceDocMetaflowGet v1_account_account_id_device_device_id_metaflow_get(account_id, device_id)

Get Device Metaflow List

Get the list of metaflows for a device.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet
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
    api_instance = openapi_client.MetaflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    device_id = 'device_id_example' # str | Device ID, 32 alpha numeric

    try:
        # Get Device Metaflow List
        api_response = api_instance.v1_account_account_id_device_device_id_metaflow_get(account_id, device_id)
        print("The response of MetaflowApi->v1_account_account_id_device_device_id_metaflow_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaflowApi->v1_account_account_id_device_device_id_metaflow_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **device_id** | **str**| Device ID, 32 alpha numeric | 

### Return type

[**ServiceDocMetaflowGet**](ServiceDocMetaflowGet.md)

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

# **v1_account_account_id_device_device_id_metaflow_post**
> ServiceDocMetaflowGet v1_account_account_id_device_device_id_metaflow_post(account_id, device_id, req_body)

Create Device Metaflow

Create a metaflow or multiple metaflows for a device.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet
from openapi_client.models.service_voip_metaflow_add_data import ServiceVOIPMetaflowAddData
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
    api_instance = openapi_client.MetaflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    device_id = 'device_id_example' # str | Device ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPMetaflowAddData() # ServiceVOIPMetaflowAddData | payload fields

    try:
        # Create Device Metaflow
        api_response = api_instance.v1_account_account_id_device_device_id_metaflow_post(account_id, device_id, req_body)
        print("The response of MetaflowApi->v1_account_account_id_device_device_id_metaflow_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaflowApi->v1_account_account_id_device_device_id_metaflow_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **device_id** | **str**| Device ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPMetaflowAddData**](ServiceVOIPMetaflowAddData.md)| payload fields | 

### Return type

[**ServiceDocMetaflowGet**](ServiceDocMetaflowGet.md)

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

# **v1_account_account_id_metaflow_delete**
> ServiceDocMetaflowGet v1_account_account_id_metaflow_delete(account_id)

Delete Account Metaflow

Remove all metaflows from an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet
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
    api_instance = openapi_client.MetaflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Delete Account Metaflow
        api_response = api_instance.v1_account_account_id_metaflow_delete(account_id)
        print("The response of MetaflowApi->v1_account_account_id_metaflow_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaflowApi->v1_account_account_id_metaflow_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocMetaflowGet**](ServiceDocMetaflowGet.md)

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

# **v1_account_account_id_metaflow_get**
> ServiceDocMetaflowGet v1_account_account_id_metaflow_get(account_id)

Get Account Metaflow List

Get an account's metaflow list.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet
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
    api_instance = openapi_client.MetaflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Account Metaflow List
        api_response = api_instance.v1_account_account_id_metaflow_get(account_id)
        print("The response of MetaflowApi->v1_account_account_id_metaflow_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaflowApi->v1_account_account_id_metaflow_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocMetaflowGet**](ServiceDocMetaflowGet.md)

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

# **v1_account_account_id_metaflow_post**
> ServiceDocMetaflowGet v1_account_account_id_metaflow_post(account_id, metaflow)

Create Account Metaflow

Generate a metaflow for an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet
from openapi_client.models.service_voip_metaflow_add_data import ServiceVOIPMetaflowAddData
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
    api_instance = openapi_client.MetaflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID
    metaflow = openapi_client.ServiceVOIPMetaflowAddData() # ServiceVOIPMetaflowAddData | Metaflow fields

    try:
        # Create Account Metaflow
        api_response = api_instance.v1_account_account_id_metaflow_post(account_id, metaflow)
        print("The response of MetaflowApi->v1_account_account_id_metaflow_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaflowApi->v1_account_account_id_metaflow_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID | 
 **metaflow** | [**ServiceVOIPMetaflowAddData**](ServiceVOIPMetaflowAddData.md)| Metaflow fields | 

### Return type

[**ServiceDocMetaflowGet**](ServiceDocMetaflowGet.md)

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

# **v1_account_account_id_user_user_id_metaflow_delete**
> ServiceDocMetaflowGet v1_account_account_id_user_user_id_metaflow_delete(account_id, user_id)

Delete User Metaflow

Delete all metaflows associated with a user.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet
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
    api_instance = openapi_client.MetaflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    user_id = 'user_id_example' # str | user ID, 32 alpha numeric

    try:
        # Delete User Metaflow
        api_response = api_instance.v1_account_account_id_user_user_id_metaflow_delete(account_id, user_id)
        print("The response of MetaflowApi->v1_account_account_id_user_user_id_metaflow_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaflowApi->v1_account_account_id_user_user_id_metaflow_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **user_id** | **str**| user ID, 32 alpha numeric | 

### Return type

[**ServiceDocMetaflowGet**](ServiceDocMetaflowGet.md)

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

# **v1_account_account_id_user_user_id_metaflow_get**
> ServiceDocMetaflowGet v1_account_account_id_user_user_id_metaflow_get(account_id, user_id)

Get User Metaflow List

Get the list of metaflows for a user.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet
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
    api_instance = openapi_client.MetaflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    user_id = 'user_id_example' # str | user ID, 32 alpha numeric

    try:
        # Get User Metaflow List
        api_response = api_instance.v1_account_account_id_user_user_id_metaflow_get(account_id, user_id)
        print("The response of MetaflowApi->v1_account_account_id_user_user_id_metaflow_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaflowApi->v1_account_account_id_user_user_id_metaflow_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **user_id** | **str**| user ID, 32 alpha numeric | 

### Return type

[**ServiceDocMetaflowGet**](ServiceDocMetaflowGet.md)

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

# **v1_account_account_id_user_user_id_metaflow_post**
> ServiceDocMetaflowGet v1_account_account_id_user_user_id_metaflow_post(account_id, user_id, req_body)

Create User Metaflow

Add a metaflow or multiple metaflows for a user in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_doc_metaflow_get import ServiceDocMetaflowGet
from openapi_client.models.service_voip_metaflow_add_data import ServiceVOIPMetaflowAddData
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
    api_instance = openapi_client.MetaflowApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    user_id = 'user_id_example' # str | user ID, 32 alpha numeric
    req_body = openapi_client.ServiceVOIPMetaflowAddData() # ServiceVOIPMetaflowAddData | payload fields

    try:
        # Create User Metaflow
        api_response = api_instance.v1_account_account_id_user_user_id_metaflow_post(account_id, user_id, req_body)
        print("The response of MetaflowApi->v1_account_account_id_user_user_id_metaflow_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaflowApi->v1_account_account_id_user_user_id_metaflow_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **user_id** | **str**| user ID, 32 alpha numeric | 
 **req_body** | [**ServiceVOIPMetaflowAddData**](ServiceVOIPMetaflowAddData.md)| payload fields | 

### Return type

[**ServiceDocMetaflowGet**](ServiceDocMetaflowGet.md)

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

