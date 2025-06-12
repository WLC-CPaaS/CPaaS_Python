# openapi_client.PhoneNumberApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_accountid_phonenumber_get**](PhoneNumberApi.md#v1_account_accountid_phonenumber_get) | **GET** /v1/account/{accountid}/phonenumber | Get Assigned Numbers List
[**v1_account_phonenumber_assign_post**](PhoneNumberApi.md#v1_account_phonenumber_assign_post) | **POST** /v1/account/phonenumber/assign | Assign Number
[**v1_account_phonenumber_disconnect_post**](PhoneNumberApi.md#v1_account_phonenumber_disconnect_post) | **POST** /v1/account/phonenumber/disconnect | Disconnect Number
[**v1_account_phonenumber_get**](PhoneNumberApi.md#v1_account_phonenumber_get) | **GET** /v1/account/phonenumber | Get Unassigned Numbers List
[**v1_account_phonenumber_post**](PhoneNumberApi.md#v1_account_phonenumber_post) | **POST** /v1/account/phonenumber | Purchase Number
[**v1_account_phonenumber_unassign_post**](PhoneNumberApi.md#v1_account_phonenumber_unassign_post) | **POST** /v1/account/phonenumber/unassign | Unassign Number
[**v1_phonenumber_search_get**](PhoneNumberApi.md#v1_phonenumber_search_get) | **GET** /v1/phonenumber/search | Search New Numbers


# **v1_account_accountid_phonenumber_get**
> ServiceDocsAccountPhonenumberGetAll v1_account_accountid_phonenumber_get(accountid, start_key=start_key, page_size=page_size)

Get Assigned Numbers List

Access all phone numbers assigned to a CPaaS account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_phonenumber_get_all import ServiceDocsAccountPhonenumberGetAll
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
    api_instance = openapi_client.PhoneNumberApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | Start key for pagination, obtained from previous responses (optional)
    page_size = 56 # int | Number of records to return per page (range: 1 to 50) (optional)

    try:
        # Get Assigned Numbers List
        api_response = api_instance.v1_account_accountid_phonenumber_get(accountid, start_key=start_key, page_size=page_size)
        print("The response of PhoneNumberApi->v1_account_accountid_phonenumber_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberApi->v1_account_accountid_phonenumber_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| Start key for pagination, obtained from previous responses | [optional] 
 **page_size** | **int**| Number of records to return per page (range: 1 to 50) | [optional] 

### Return type

[**ServiceDocsAccountPhonenumberGetAll**](ServiceDocsAccountPhonenumberGetAll.md)

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

# **v1_account_phonenumber_assign_post**
> ServiceAPIResponseStatusCodeOnly v1_account_phonenumber_assign_post(payload)

Assign Number

Assign a purchased phone number to an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response_status_code_only import ServiceAPIResponseStatusCodeOnly
from openapi_client.models.service_docs_phonenumber_assign_payload import ServiceDocsPhonenumberAssignPayload
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
    api_instance = openapi_client.PhoneNumberApi(api_client)
    payload = openapi_client.ServiceDocsPhonenumberAssignPayload() # ServiceDocsPhonenumberAssignPayload | assignment payload

    try:
        # Assign Number
        api_response = api_instance.v1_account_phonenumber_assign_post(payload)
        print("The response of PhoneNumberApi->v1_account_phonenumber_assign_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberApi->v1_account_phonenumber_assign_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ServiceDocsPhonenumberAssignPayload**](ServiceDocsPhonenumberAssignPayload.md)| assignment payload | 

### Return type

[**ServiceAPIResponseStatusCodeOnly**](ServiceAPIResponseStatusCodeOnly.md)

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

# **v1_account_phonenumber_disconnect_post**
> ServiceAPIResponseStatusCodeOnly v1_account_phonenumber_disconnect_post(payload)

Disconnect Number

Disconnecting a phone number from a CPaaS account relinquishes ownership of the number back to the carrier.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response_status_code_only import ServiceAPIResponseStatusCodeOnly
from openapi_client.models.service_docs_phonenumber_unassign_payload import ServiceDocsPhonenumberUnassignPayload
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
    api_instance = openapi_client.PhoneNumberApi(api_client)
    payload = openapi_client.ServiceDocsPhonenumberUnassignPayload() # ServiceDocsPhonenumberUnassignPayload | disconnect payload

    try:
        # Disconnect Number
        api_response = api_instance.v1_account_phonenumber_disconnect_post(payload)
        print("The response of PhoneNumberApi->v1_account_phonenumber_disconnect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberApi->v1_account_phonenumber_disconnect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ServiceDocsPhonenumberUnassignPayload**](ServiceDocsPhonenumberUnassignPayload.md)| disconnect payload | 

### Return type

[**ServiceAPIResponseStatusCodeOnly**](ServiceAPIResponseStatusCodeOnly.md)

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

# **v1_account_phonenumber_get**
> ServiceDocsAccountPhonenumberGetAll v1_account_phonenumber_get(start_key=start_key, page_size=page_size)

Get Unassigned Numbers List

Obtain all phone numbers that have not been assigned to a CPaaS account within your organization.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_phonenumber_get_all import ServiceDocsAccountPhonenumberGetAll
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
    api_instance = openapi_client.PhoneNumberApi(api_client)
    start_key = 'start_key_example' # str | Start key for pagination, obtained from previous responses (optional)
    page_size = 56 # int | Number of records to return per page (range: 1 to 50) (optional)

    try:
        # Get Unassigned Numbers List
        api_response = api_instance.v1_account_phonenumber_get(start_key=start_key, page_size=page_size)
        print("The response of PhoneNumberApi->v1_account_phonenumber_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberApi->v1_account_phonenumber_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_key** | **str**| Start key for pagination, obtained from previous responses | [optional] 
 **page_size** | **int**| Number of records to return per page (range: 1 to 50) | [optional] 

### Return type

[**ServiceDocsAccountPhonenumberGetAll**](ServiceDocsAccountPhonenumberGetAll.md)

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

# **v1_account_phonenumber_post**
> ServiceDocsOrderPhonenumber v1_account_phonenumber_post(phonenumber)

Purchase Number

Purchase or activate a phone number for CPaaS accounts within your business.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_order_phonenumber import ServiceDocsOrderPhonenumber
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
    api_instance = openapi_client.PhoneNumberApi(api_client)
    phonenumber = ['phonenumber_example'] # List[str] | phonenumber fields

    try:
        # Purchase Number
        api_response = api_instance.v1_account_phonenumber_post(phonenumber)
        print("The response of PhoneNumberApi->v1_account_phonenumber_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberApi->v1_account_phonenumber_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phonenumber** | [**List[str]**](str.md)| phonenumber fields | 

### Return type

[**ServiceDocsOrderPhonenumber**](ServiceDocsOrderPhonenumber.md)

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

# **v1_account_phonenumber_unassign_post**
> ServiceAPIResponseStatusCodeOnly v1_account_phonenumber_unassign_post(payload)

Unassign Number

Remove a phone number from an account and place it back on the list of unassigned phone numbers.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_api_response_status_code_only import ServiceAPIResponseStatusCodeOnly
from openapi_client.models.service_docs_phonenumber_unassign_payload import ServiceDocsPhonenumberUnassignPayload
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
    api_instance = openapi_client.PhoneNumberApi(api_client)
    payload = openapi_client.ServiceDocsPhonenumberUnassignPayload() # ServiceDocsPhonenumberUnassignPayload | unassign payload

    try:
        # Unassign Number
        api_response = api_instance.v1_account_phonenumber_unassign_post(payload)
        print("The response of PhoneNumberApi->v1_account_phonenumber_unassign_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberApi->v1_account_phonenumber_unassign_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ServiceDocsPhonenumberUnassignPayload**](ServiceDocsPhonenumberUnassignPayload.md)| unassign payload | 

### Return type

[**ServiceAPIResponseStatusCodeOnly**](ServiceAPIResponseStatusCodeOnly.md)

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

# **v1_phonenumber_search_get**
> ServiceDocsPhonenumberSearchGetAll v1_phonenumber_search_get(area_code, quantity=quantity)

Search New Numbers

Conduct a search for available phone numbers for purchase within an area code.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_phonenumber_search_get_all import ServiceDocsPhonenumberSearchGetAll
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
    api_instance = openapi_client.PhoneNumberApi(api_client)
    area_code = 'area_code_example' # str | Area code (exactly 3 numeric characters) example: 610 or 484
    quantity = 100 # int | Number of records to return (range: 1 to 100, defaults to 100 if not provided) (optional) (default to 100)

    try:
        # Search New Numbers
        api_response = api_instance.v1_phonenumber_search_get(area_code, quantity=quantity)
        print("The response of PhoneNumberApi->v1_phonenumber_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberApi->v1_phonenumber_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_code** | **str**| Area code (exactly 3 numeric characters) example: 610 or 484 | 
 **quantity** | **int**| Number of records to return (range: 1 to 100, defaults to 100 if not provided) | [optional] [default to 100]

### Return type

[**ServiceDocsPhonenumberSearchGetAll**](ServiceDocsPhonenumberSearchGetAll.md)

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

