# openapi_client.CPaaSManagementApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_mgmt_user_get**](CPaaSManagementApi.md#v1_mgmt_user_get) | **GET** /v1/mgmt/user | Get All CPaaS Users
[**v1_mgmt_user_post**](CPaaSManagementApi.md#v1_mgmt_user_post) | **POST** /v1/mgmt/user | Invite CPaaS User
[**v1_mgmt_user_user_id_delete**](CPaaSManagementApi.md#v1_mgmt_user_user_id_delete) | **DELETE** /v1/mgmt/user/{userID} | Delete CPaaS User
[**v1_mgmt_user_user_id_get**](CPaaSManagementApi.md#v1_mgmt_user_user_id_get) | **GET** /v1/mgmt/user/{userID} | Get CPaaS User Details
[**v1_mgmt_user_user_id_put**](CPaaSManagementApi.md#v1_mgmt_user_user_id_put) | **PUT** /v1/mgmt/user/{userID} | Update CPaaS User Role


# **v1_mgmt_user_get**
> ServiceDocsAdminUserGetAll v1_mgmt_user_get(page_size=page_size, start_key=start_key, sort=sort, email=email, role=role, first_name=first_name, last_name=last_name)

Get All CPaaS Users

Retrieve a list of all CPaaS users in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_admin_user_get_all import ServiceDocsAdminUserGetAll
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
    api_instance = openapi_client.CPaaSManagementApi(api_client)
    page_size = 56 # int | number of records to return, range 1 to 100 (optional)
    start_key = 'start_key_example' # str | unique to fetch next records (optional)
    sort = 'sort_example' # str | sorting the records by email(default)/role/first_name/last_name, _A is for ascending and _D is for descending, eg: sort=role_A,email_D (optional)
    email = 'email_example' # str | Email (optional)
    role = 'role_example' # str | User Role (optional)
    first_name = 'first_name_example' # str | First Name (optional)
    last_name = 'last_name_example' # str | Last Name (optional)

    try:
        # Get All CPaaS Users
        api_response = api_instance.v1_mgmt_user_get(page_size=page_size, start_key=start_key, sort=sort, email=email, role=role, first_name=first_name, last_name=last_name)
        print("The response of CPaaSManagementApi->v1_mgmt_user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPaaSManagementApi->v1_mgmt_user_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| number of records to return, range 1 to 100 | [optional] 
 **start_key** | **str**| unique to fetch next records | [optional] 
 **sort** | **str**| sorting the records by email(default)/role/first_name/last_name, _A is for ascending and _D is for descending, eg: sort&#x3D;role_A,email_D | [optional] 
 **email** | **str**| Email | [optional] 
 **role** | **str**| User Role | [optional] 
 **first_name** | **str**| First Name | [optional] 
 **last_name** | **str**| Last Name | [optional] 

### Return type

[**ServiceDocsAdminUserGetAll**](ServiceDocsAdminUserGetAll.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_mgmt_user_post**
> ServiceDocsAdminUserGetSingle v1_mgmt_user_post(req_body)

Invite CPaaS User

Link a new CPaaS user to an existing client account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_admin_user_add_data import ServiceAdminUserAddData
from openapi_client.models.service_docs_admin_user_get_single import ServiceDocsAdminUserGetSingle
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
    api_instance = openapi_client.CPaaSManagementApi(api_client)
    req_body = openapi_client.ServiceAdminUserAddData() # ServiceAdminUserAddData | payload fields

    try:
        # Invite CPaaS User
        api_response = api_instance.v1_mgmt_user_post(req_body)
        print("The response of CPaaSManagementApi->v1_mgmt_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPaaSManagementApi->v1_mgmt_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_body** | [**ServiceAdminUserAddData**](ServiceAdminUserAddData.md)| payload fields | 

### Return type

[**ServiceDocsAdminUserGetSingle**](ServiceDocsAdminUserGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_mgmt_user_user_id_delete**
> ServiceDocsAdminUserDelete v1_mgmt_user_user_id_delete(user_id)

Delete CPaaS User

Delete a CPaaS user from the associated account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_admin_user_delete import ServiceDocsAdminUserDelete
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
    api_instance = openapi_client.CPaaSManagementApi(api_client)
    user_id = 'user_id_example' # str | User ID, numeric

    try:
        # Delete CPaaS User
        api_response = api_instance.v1_mgmt_user_user_id_delete(user_id)
        print("The response of CPaaSManagementApi->v1_mgmt_user_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPaaSManagementApi->v1_mgmt_user_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID, numeric | 

### Return type

[**ServiceDocsAdminUserDelete**](ServiceDocsAdminUserDelete.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_mgmt_user_user_id_get**
> ServiceDocsAdminUserGetSingle v1_mgmt_user_user_id_get(user_id)

Get CPaaS User Details

View details about each CPaaS user in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_admin_user_get_single import ServiceDocsAdminUserGetSingle
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
    api_instance = openapi_client.CPaaSManagementApi(api_client)
    user_id = 'user_id_example' # str | User ID, numeric

    try:
        # Get CPaaS User Details
        api_response = api_instance.v1_mgmt_user_user_id_get(user_id)
        print("The response of CPaaSManagementApi->v1_mgmt_user_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPaaSManagementApi->v1_mgmt_user_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID, numeric | 

### Return type

[**ServiceDocsAdminUserGetSingle**](ServiceDocsAdminUserGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_mgmt_user_user_id_put**
> ServiceDocsAdminUserGetSingle v1_mgmt_user_user_id_put(user_id, req_body)

Update CPaaS User Role

Update a CPaaS user's role within a client's account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_admin_user_edit_data import ServiceAdminUserEditData
from openapi_client.models.service_docs_admin_user_get_single import ServiceDocsAdminUserGetSingle
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
    api_instance = openapi_client.CPaaSManagementApi(api_client)
    user_id = 'user_id_example' # str | User ID, numeric
    req_body = openapi_client.ServiceAdminUserEditData() # ServiceAdminUserEditData | payload fields

    try:
        # Update CPaaS User Role
        api_response = api_instance.v1_mgmt_user_user_id_put(user_id, req_body)
        print("The response of CPaaSManagementApi->v1_mgmt_user_user_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPaaSManagementApi->v1_mgmt_user_user_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID, numeric | 
 **req_body** | [**ServiceAdminUserEditData**](ServiceAdminUserEditData.md)| payload fields | 

### Return type

[**ServiceDocsAdminUserGetSingle**](ServiceDocsAdminUserGetSingle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

