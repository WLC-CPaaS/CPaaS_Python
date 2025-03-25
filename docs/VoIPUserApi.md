# openapi_client.VoIPUserApi

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_accountid_user_get**](VoIPUserApi.md#v1_account_accountid_user_get) | **GET** /v1/account/{accountid}/user | Get User List
[**v1_account_accountid_user_post**](VoIPUserApi.md#v1_account_accountid_user_post) | **POST** /v1/account/{accountid}/user | Create User
[**v1_account_accountid_user_userid_delete**](VoIPUserApi.md#v1_account_accountid_user_userid_delete) | **DELETE** /v1/account/{accountid}/user/{userid} | Delete User
[**v1_account_accountid_user_userid_get**](VoIPUserApi.md#v1_account_accountid_user_userid_get) | **GET** /v1/account/{accountid}/user/{userid} | Get User Details
[**v1_account_accountid_user_userid_put**](VoIPUserApi.md#v1_account_accountid_user_userid_put) | **PUT** /v1/account/{accountid}/user/{userid} | Update User


# **v1_account_accountid_user_get**
> ServiceDocsUserGetAll v1_account_accountid_user_get(accountid, start_key=start_key, page_size=page_size)

Get User List

Get a list of all VoIP users that includes first and last names, email addresses, extensions, and account statuses.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_user_get_all import ServiceDocsUserGetAll
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
    api_instance = openapi_client.VoIPUserApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get User List
        api_response = api_instance.v1_account_accountid_user_get(accountid, start_key=start_key, page_size=page_size)
        print("The response of VoIPUserApi->v1_account_accountid_user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoIPUserApi->v1_account_accountid_user_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsUserGetAll**](ServiceDocsUserGetAll.md)

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

# **v1_account_accountid_user_post**
> ServiceDocsUserGetSingle v1_account_accountid_user_post(accountid, user)

Create User

Add new users to the account. When a user is added, the system generates their unique 32 alpha numeric ID.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_user_get_single import ServiceDocsUserGetSingle
from openapi_client.models.service_voip_user_add2 import ServiceVOIPUserAdd2
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
    api_instance = openapi_client.VoIPUserApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    user = openapi_client.ServiceVOIPUserAdd2() # ServiceVOIPUserAdd2 | user fields

    try:
        # Create User
        api_response = api_instance.v1_account_accountid_user_post(accountid, user)
        print("The response of VoIPUserApi->v1_account_accountid_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoIPUserApi->v1_account_accountid_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **user** | [**ServiceVOIPUserAdd2**](ServiceVOIPUserAdd2.md)| user fields | 

### Return type

[**ServiceDocsUserGetSingle**](ServiceDocsUserGetSingle.md)

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

# **v1_account_accountid_user_userid_delete**
> ServiceDocsUserGetSingle v1_account_accountid_user_userid_delete(accountid, userid)

Delete User

Delete VoIP user access to maintain the security of your accounts.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_user_get_single import ServiceDocsUserGetSingle
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
    api_instance = openapi_client.VoIPUserApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    userid = 'userid_example' # str | User ID, 32 alpha numeric

    try:
        # Delete User
        api_response = api_instance.v1_account_accountid_user_userid_delete(accountid, userid)
        print("The response of VoIPUserApi->v1_account_accountid_user_userid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoIPUserApi->v1_account_accountid_user_userid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **userid** | **str**| User ID, 32 alpha numeric | 

### Return type

[**ServiceDocsUserGetSingle**](ServiceDocsUserGetSingle.md)

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

# **v1_account_accountid_user_userid_get**
> ServiceDocsUserGetSingle v1_account_accountid_user_userid_get(accountid, userid)

Get User Details

View specific user details.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_user_get_single import ServiceDocsUserGetSingle
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
    api_instance = openapi_client.VoIPUserApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    userid = 'userid_example' # str | User ID, 32 alpha numeric

    try:
        # Get User Details
        api_response = api_instance.v1_account_accountid_user_userid_get(accountid, userid)
        print("The response of VoIPUserApi->v1_account_accountid_user_userid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoIPUserApi->v1_account_accountid_user_userid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **userid** | **str**| User ID, 32 alpha numeric | 

### Return type

[**ServiceDocsUserGetSingle**](ServiceDocsUserGetSingle.md)

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

# **v1_account_accountid_user_userid_put**
> ServiceDocsUserGetSingle v1_account_accountid_user_userid_put(accountid, userid, user)

Update User

Keep user information current. Modify the first and last name, extension, and other pertinent information.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_user_get_single import ServiceDocsUserGetSingle
from openapi_client.models.service_voip_user_add2 import ServiceVOIPUserAdd2
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
    api_instance = openapi_client.VoIPUserApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    userid = 'userid_example' # str | User ID, 32 alpha numeric
    user = openapi_client.ServiceVOIPUserAdd2() # ServiceVOIPUserAdd2 | user fields

    try:
        # Update User
        api_response = api_instance.v1_account_accountid_user_userid_put(accountid, userid, user)
        print("The response of VoIPUserApi->v1_account_accountid_user_userid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoIPUserApi->v1_account_accountid_user_userid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **userid** | **str**| User ID, 32 alpha numeric | 
 **user** | [**ServiceVOIPUserAdd2**](ServiceVOIPUserAdd2.md)| user fields | 

### Return type

[**ServiceDocsUserGetSingle**](ServiceDocsUserGetSingle.md)

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

