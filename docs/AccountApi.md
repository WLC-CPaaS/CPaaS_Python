# openapi_client.AccountApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_accountid_children_get**](AccountApi.md#v1_account_accountid_children_get) | **GET** /v1/account/{accountid}/children | Get Sub Account List
[**v1_account_accountid_delete**](AccountApi.md#v1_account_accountid_delete) | **DELETE** /v1/account/{accountid} | Delete Account
[**v1_account_accountid_dnsrecord_get**](AccountApi.md#v1_account_accountid_dnsrecord_get) | **GET** /v1/account/{accountid}/dnsrecord | Get Account DNS Record
[**v1_account_accountid_dnsrecord_post**](AccountApi.md#v1_account_accountid_dnsrecord_post) | **POST** /v1/account/{accountid}/dnsrecord | Create Account DNS Record
[**v1_account_accountid_dnsrecord_put**](AccountApi.md#v1_account_accountid_dnsrecord_put) | **PUT** /v1/account/{accountid}/dnsrecord | Convert Account DNS Record
[**v1_account_accountid_get**](AccountApi.md#v1_account_accountid_get) | **GET** /v1/account/{accountid} | Get Account Details
[**v1_account_accountid_limit_get**](AccountApi.md#v1_account_accountid_limit_get) | **GET** /v1/account/{accountid}/limit | Get Account Limits
[**v1_account_accountid_limit_put**](AccountApi.md#v1_account_accountid_limit_put) | **PUT** /v1/account/{accountid}/limit | Set Account Limits
[**v1_account_accountid_post**](AccountApi.md#v1_account_accountid_post) | **POST** /v1/account/{accountid} | Create Sub Account
[**v1_account_accountid_provisioningdetails_get**](AccountApi.md#v1_account_accountid_provisioningdetails_get) | **GET** /v1/account/{accountid}/provisioningdetails | Get Account Provisioning Details
[**v1_account_accountid_provisioningdetails_resetpw_put**](AccountApi.md#v1_account_accountid_provisioningdetails_resetpw_put) | **PUT** /v1/account/{accountid}/provisioningdetails/resetpw | Reset the provisioning details password.
[**v1_account_accountid_put**](AccountApi.md#v1_account_accountid_put) | **PUT** /v1/account/{accountid} | Update Account
[**v1_account_apikey_get**](AccountApi.md#v1_account_apikey_get) | **GET** /v1/account/apikey | 
[**v1_account_get**](AccountApi.md#v1_account_get) | **GET** /v1/account | Get Account List
[**v1_account_post**](AccountApi.md#v1_account_post) | **POST** /v1/account | Create Account


# **v1_account_accountid_children_get**
> ServiceDocsAccountGetAll v1_account_accountid_children_get(accountid, start_key=start_key, page_size=page_size)

Get Sub Account List

Conveniently access the list of children accounts.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_all import ServiceDocsAccountGetAll
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Sub Account List
        api_response = api_instance.v1_account_accountid_children_get(accountid, start_key=start_key, page_size=page_size)
        print("The response of AccountApi->v1_account_accountid_children_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_children_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsAccountGetAll**](ServiceDocsAccountGetAll.md)

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

# **v1_account_accountid_delete**
> ServiceDocsAccountGetSingle v1_account_accountid_delete(accountid)

Delete Account

Delete an account within your organization.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_single import ServiceDocsAccountGetSingle
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric

    try:
        # Delete Account
        api_response = api_instance.v1_account_accountid_delete(accountid)
        print("The response of AccountApi->v1_account_accountid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsAccountGetSingle**](ServiceDocsAccountGetSingle.md)

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

# **v1_account_accountid_dnsrecord_get**
> ServiceDocsAccountGetSingle v1_account_accountid_dnsrecord_get(accountid)

Get Account DNS Record

Get the DNS record of an account from the Route 53 entry.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_single import ServiceDocsAccountGetSingle
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Account DNS Record
        api_response = api_instance.v1_account_accountid_dnsrecord_get(accountid)
        print("The response of AccountApi->v1_account_accountid_dnsrecord_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_dnsrecord_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsAccountGetSingle**](ServiceDocsAccountGetSingle.md)

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

# **v1_account_accountid_dnsrecord_post**
> ServiceDocsAccountGetSingle v1_account_accountid_dnsrecord_post(accountid)

Create Account DNS Record

Create the DNS record of an account with the help realm in the Route 53 entry.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_single import ServiceDocsAccountGetSingle
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric

    try:
        # Create Account DNS Record
        api_response = api_instance.v1_account_accountid_dnsrecord_post(accountid)
        print("The response of AccountApi->v1_account_accountid_dnsrecord_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_dnsrecord_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsAccountGetSingle**](ServiceDocsAccountGetSingle.md)

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

# **v1_account_accountid_dnsrecord_put**
> ServiceDocsAccountGetSingle v1_account_accountid_dnsrecord_put(accountid, dnsrecord)

Convert Account DNS Record

Toggle the realm DNS record between srv and cname.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_single import ServiceDocsAccountGetSingle
from openapi_client.models.service_update_record_type_for_account import ServiceUpdateRecordTypeForAccount
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    dnsrecord = openapi_client.ServiceUpdateRecordTypeForAccount() # ServiceUpdateRecordTypeForAccount | record type fields with value SRV, CNAME

    try:
        # Convert Account DNS Record
        api_response = api_instance.v1_account_accountid_dnsrecord_put(accountid, dnsrecord)
        print("The response of AccountApi->v1_account_accountid_dnsrecord_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_dnsrecord_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **dnsrecord** | [**ServiceUpdateRecordTypeForAccount**](ServiceUpdateRecordTypeForAccount.md)| record type fields with value SRV, CNAME | 

### Return type

[**ServiceDocsAccountGetSingle**](ServiceDocsAccountGetSingle.md)

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

# **v1_account_accountid_get**
> ServiceDocsAccountGetSingle v1_account_accountid_get(accountid)

Get Account Details

This endpoint will not allow for modifying or making updates, it will only allow users to view/retrieve details.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_single import ServiceDocsAccountGetSingle
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Account Details
        api_response = api_instance.v1_account_accountid_get(accountid)
        print("The response of AccountApi->v1_account_accountid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsAccountGetSingle**](ServiceDocsAccountGetSingle.md)

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

# **v1_account_accountid_limit_get**
> ServiceDocsAccountLimit v1_account_accountid_limit_get(accountid)

Get Account Limits

Check the maximum number of inbound, outbound, and two-way trunks.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_limit import ServiceDocsAccountLimit
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Account Limits
        api_response = api_instance.v1_account_accountid_limit_get(accountid)
        print("The response of AccountApi->v1_account_accountid_limit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_limit_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsAccountLimit**](ServiceDocsAccountLimit.md)

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

# **v1_account_accountid_limit_put**
> ServiceDocsAccountLimit v1_account_accountid_limit_put(accountid, limit)

Set Account Limits

Apply parameters to restrict access to inbound, outbound, and two-way trunks.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_limit import ServiceDocsAccountLimit
from openapi_client.models.service_voip_account_limit2 import ServiceVOIPAccountLimit2
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    limit = openapi_client.ServiceVOIPAccountLimit2() # ServiceVOIPAccountLimit2 | account fields

    try:
        # Set Account Limits
        api_response = api_instance.v1_account_accountid_limit_put(accountid, limit)
        print("The response of AccountApi->v1_account_accountid_limit_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_limit_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **limit** | [**ServiceVOIPAccountLimit2**](ServiceVOIPAccountLimit2.md)| account fields | 

### Return type

[**ServiceDocsAccountLimit**](ServiceDocsAccountLimit.md)

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

# **v1_account_accountid_post**
> ServiceDocsAccountGetSingle v1_account_accountid_post(accountid, account)

Create Sub Account

Establish a sub account to enable an administrator within your organization to create accounts.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_single import ServiceDocsAccountGetSingle
from openapi_client.models.service_voip_account_add_data import ServiceVOIPAccountAddData
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    account = openapi_client.ServiceVOIPAccountAddData() # ServiceVOIPAccountAddData | account fields

    try:
        # Create Sub Account
        api_response = api_instance.v1_account_accountid_post(accountid, account)
        print("The response of AccountApi->v1_account_accountid_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **account** | [**ServiceVOIPAccountAddData**](ServiceVOIPAccountAddData.md)| account fields | 

### Return type

[**ServiceDocsAccountGetSingle**](ServiceDocsAccountGetSingle.md)

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

# **v1_account_accountid_provisioningdetails_get**
> ServiceDocsAccountProvisioning v1_account_accountid_provisioningdetails_get(accountid)

Get Account Provisioning Details

Get the provisioning details of an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_provisioning import ServiceDocsAccountProvisioning
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Account Provisioning Details
        api_response = api_instance.v1_account_accountid_provisioningdetails_get(accountid)
        print("The response of AccountApi->v1_account_accountid_provisioningdetails_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_provisioningdetails_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsAccountProvisioning**](ServiceDocsAccountProvisioning.md)

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

# **v1_account_accountid_provisioningdetails_resetpw_put**
> ServiceDocsAccountProvisioning v1_account_accountid_provisioningdetails_resetpw_put(accountid)

Reset the provisioning details password.

Reset the existing provisioning details password and set it to a new one.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_provisioning import ServiceDocsAccountProvisioning
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric

    try:
        # Reset the provisioning details password.
        api_response = api_instance.v1_account_accountid_provisioningdetails_resetpw_put(accountid)
        print("The response of AccountApi->v1_account_accountid_provisioningdetails_resetpw_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_provisioningdetails_resetpw_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsAccountProvisioning**](ServiceDocsAccountProvisioning.md)

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

# **v1_account_accountid_put**
> ServiceDocsAccountGetSingle v1_account_accountid_put(accountid, account)

Update Account

Modify pertinent account data.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_single import ServiceDocsAccountGetSingle
from openapi_client.models.service_voip_account_edit_data import ServiceVOIPAccountEditData
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
    api_instance = openapi_client.AccountApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    account = openapi_client.ServiceVOIPAccountEditData() # ServiceVOIPAccountEditData | account fields

    try:
        # Update Account
        api_response = api_instance.v1_account_accountid_put(accountid, account)
        print("The response of AccountApi->v1_account_accountid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_accountid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **account** | [**ServiceVOIPAccountEditData**](ServiceVOIPAccountEditData.md)| account fields | 

### Return type

[**ServiceDocsAccountGetSingle**](ServiceDocsAccountGetSingle.md)

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

# **v1_account_apikey_get**
> ServiceDocsAccountAPIKey v1_account_apikey_get()

Authenticate an application or user request to get the client ID and client secret for a CPaaS account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_api_key import ServiceDocsAccountAPIKey
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
    api_instance = openapi_client.AccountApi(api_client)

    try:
        api_response = api_instance.v1_account_apikey_get()
        print("The response of AccountApi->v1_account_apikey_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_apikey_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceDocsAccountAPIKey**](ServiceDocsAccountAPIKey.md)

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

# **v1_account_get**
> ServiceDocsAccountGetAll v1_account_get(start_key=start_key, page_size=page_size)

Get Account List

Retrieve a list of all CPaaS accounts that exist within your organization.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_all import ServiceDocsAccountGetAll
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
    api_instance = openapi_client.AccountApi(api_client)
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Account List
        api_response = api_instance.v1_account_get(start_key=start_key, page_size=page_size)
        print("The response of AccountApi->v1_account_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsAccountGetAll**](ServiceDocsAccountGetAll.md)

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

# **v1_account_post**
> ServiceDocsAccountGetSingle v1_account_post(account)

Create Account

Create an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_account_get_single import ServiceDocsAccountGetSingle
from openapi_client.models.service_voip_account_add_data import ServiceVOIPAccountAddData
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
    api_instance = openapi_client.AccountApi(api_client)
    account = openapi_client.ServiceVOIPAccountAddData() # ServiceVOIPAccountAddData | account fields

    try:
        # Create Account
        api_response = api_instance.v1_account_post(account)
        print("The response of AccountApi->v1_account_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**ServiceVOIPAccountAddData**](ServiceVOIPAccountAddData.md)| account fields | 

### Return type

[**ServiceDocsAccountGetSingle**](ServiceDocsAccountGetSingle.md)

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

