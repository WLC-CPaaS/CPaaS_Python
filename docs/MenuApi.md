# openapi_client.MenuApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_account_id_menu_get**](MenuApi.md#v1_account_account_id_menu_get) | **GET** /v1/account/{accountID}/menu | Get Menu List
[**v1_account_account_id_menu_menu_id_delete**](MenuApi.md#v1_account_account_id_menu_menu_id_delete) | **DELETE** /v1/account/{accountID}/menu/{menuID} | Delete Menu
[**v1_account_account_id_menu_menu_id_get**](MenuApi.md#v1_account_account_id_menu_menu_id_get) | **GET** /v1/account/{accountID}/menu/{menuID} | Get Menu Details
[**v1_account_account_id_menu_menu_id_put**](MenuApi.md#v1_account_account_id_menu_menu_id_put) | **PUT** /v1/account/{accountID}/menu/{menuID} | Update Menu
[**v1_account_account_id_menu_post**](MenuApi.md#v1_account_account_id_menu_post) | **POST** /v1/account/{accountID}/menu | Create Menu


# **v1_account_account_id_menu_get**
> MenuOutputList v1_account_account_id_menu_get(account_id, start_key=start_key, page_size=page_size)

Get Menu List

Users can access data about all menus in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.menu_output_list import MenuOutputList
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
    api_instance = openapi_client.MenuApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Menu List
        api_response = api_instance.v1_account_account_id_menu_get(account_id, start_key=start_key, page_size=page_size)
        print("The response of MenuApi->v1_account_account_id_menu_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->v1_account_account_id_menu_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**MenuOutputList**](MenuOutputList.md)

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

# **v1_account_account_id_menu_menu_id_delete**
> MenuOutputDetail v1_account_account_id_menu_menu_id_delete(account_id, menu_id)

Delete Menu

Delete a menu from an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.menu_output_detail import MenuOutputDetail
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
    api_instance = openapi_client.MenuApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    menu_id = 'menu_id_example' # str | Menu ID, 32 alpha numeric

    try:
        # Delete Menu
        api_response = api_instance.v1_account_account_id_menu_menu_id_delete(account_id, menu_id)
        print("The response of MenuApi->v1_account_account_id_menu_menu_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->v1_account_account_id_menu_menu_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **menu_id** | **str**| Menu ID, 32 alpha numeric | 

### Return type

[**MenuOutputDetail**](MenuOutputDetail.md)

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

# **v1_account_account_id_menu_menu_id_get**
> MenuOutputDetail v1_account_account_id_menu_menu_id_get(account_id, menu_id)

Get Menu Details

Get details about a menu in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.menu_output_detail import MenuOutputDetail
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
    api_instance = openapi_client.MenuApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    menu_id = 'menu_id_example' # str | Menu ID, 32 alpha numeric

    try:
        # Get Menu Details
        api_response = api_instance.v1_account_account_id_menu_menu_id_get(account_id, menu_id)
        print("The response of MenuApi->v1_account_account_id_menu_menu_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->v1_account_account_id_menu_menu_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **menu_id** | **str**| Menu ID, 32 alpha numeric | 

### Return type

[**MenuOutputDetail**](MenuOutputDetail.md)

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

# **v1_account_account_id_menu_menu_id_put**
> MenuOutputDetail v1_account_account_id_menu_menu_id_put(account_id, menu_id, req_body)

Update Menu

Edit an account menu.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.menu_input_data import MenuInputData
from openapi_client.models.menu_output_detail import MenuOutputDetail
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
    api_instance = openapi_client.MenuApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alpha numeric
    menu_id = 'menu_id_example' # str | Menu ID, 32 alpha numeric
    req_body = openapi_client.MenuInputData() # MenuInputData | payload fields

    try:
        # Update Menu
        api_response = api_instance.v1_account_account_id_menu_menu_id_put(account_id, menu_id, req_body)
        print("The response of MenuApi->v1_account_account_id_menu_menu_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->v1_account_account_id_menu_menu_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alpha numeric | 
 **menu_id** | **str**| Menu ID, 32 alpha numeric | 
 **req_body** | [**MenuInputData**](MenuInputData.md)| payload fields | 

### Return type

[**MenuOutputDetail**](MenuOutputDetail.md)

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

# **v1_account_account_id_menu_post**
> MenuOutputDetail v1_account_account_id_menu_post(account_id, menu)

Create Menu

Create a new menu for an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.menu_input_data import MenuInputData
from openapi_client.models.menu_output_detail import MenuOutputDetail
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
    api_instance = openapi_client.MenuApi(api_client)
    account_id = 'account_id_example' # str | Account ID, 32 alphanumeric
    menu = openapi_client.MenuInputData() # MenuInputData | Menu data

    try:
        # Create Menu
        api_response = api_instance.v1_account_account_id_menu_post(account_id, menu)
        print("The response of MenuApi->v1_account_account_id_menu_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->v1_account_account_id_menu_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID, 32 alphanumeric | 
 **menu** | [**MenuInputData**](MenuInputData.md)| Menu data | 

### Return type

[**MenuOutputDetail**](MenuOutputDetail.md)

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

