# openapi_client.DeviceApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_accountid_device_deviceid_delete**](DeviceApi.md#v1_account_accountid_device_deviceid_delete) | **DELETE** /v1/account/{accountid}/device/{deviceid} | Delete Device
[**v1_account_accountid_device_deviceid_get**](DeviceApi.md#v1_account_accountid_device_deviceid_get) | **GET** /v1/account/{accountid}/device/{deviceid} | Get Device Details
[**v1_account_accountid_device_deviceid_put**](DeviceApi.md#v1_account_accountid_device_deviceid_put) | **PUT** /v1/account/{accountid}/device/{deviceid} | Update Device
[**v1_account_accountid_device_deviceid_reboot_post**](DeviceApi.md#v1_account_accountid_device_deviceid_reboot_post) | **POST** /v1/account/{accountid}/device/{deviceid}/reboot | Reboot Device
[**v1_account_accountid_device_get**](DeviceApi.md#v1_account_accountid_device_get) | **GET** /v1/account/{accountid}/device | Get Device List
[**v1_account_accountid_device_post**](DeviceApi.md#v1_account_accountid_device_post) | **POST** /v1/account/{accountid}/device | Create Device
[**v1_account_accountid_device_status_get**](DeviceApi.md#v1_account_accountid_device_status_get) | **GET** /v1/account/{accountid}/device/status | Get Device Status


# **v1_account_accountid_device_deviceid_delete**
> ServiceDocsDeviceGetSingle v1_account_accountid_device_deviceid_delete(accountid, deviceid)

Delete Device

Remove one device from a CPaaS account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_device_get_single import ServiceDocsDeviceGetSingle
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
    api_instance = openapi_client.DeviceApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    deviceid = 'deviceid_example' # str | Device ID, 32 alpha numeric

    try:
        # Delete Device
        api_response = api_instance.v1_account_accountid_device_deviceid_delete(accountid, deviceid)
        print("The response of DeviceApi->v1_account_accountid_device_deviceid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->v1_account_accountid_device_deviceid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **deviceid** | **str**| Device ID, 32 alpha numeric | 

### Return type

[**ServiceDocsDeviceGetSingle**](ServiceDocsDeviceGetSingle.md)

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

# **v1_account_accountid_device_deviceid_get**
> ServiceDocsDeviceGetSingle v1_account_accountid_device_deviceid_get(accountid, deviceid)

Get Device Details

Permit a user to view specific device details.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_device_get_single import ServiceDocsDeviceGetSingle
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
    api_instance = openapi_client.DeviceApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    deviceid = 'deviceid_example' # str | Device ID, 32 alpha numeric

    try:
        # Get Device Details
        api_response = api_instance.v1_account_accountid_device_deviceid_get(accountid, deviceid)
        print("The response of DeviceApi->v1_account_accountid_device_deviceid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->v1_account_accountid_device_deviceid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **deviceid** | **str**| Device ID, 32 alpha numeric | 

### Return type

[**ServiceDocsDeviceGetSingle**](ServiceDocsDeviceGetSingle.md)

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

# **v1_account_accountid_device_deviceid_put**
> ServiceDocsDeviceGetSingle v1_account_accountid_device_deviceid_put(accountid, deviceid, device)

Update Device

Edit specifics about the device, such as the device type, name, and owner.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_device_get_single import ServiceDocsDeviceGetSingle
from openapi_client.models.service_voip_device_add_edit2 import ServiceVOIPDeviceAddEdit2
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
    api_instance = openapi_client.DeviceApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    deviceid = 'deviceid_example' # str | Device ID, 32 alpha numeric
    device = openapi_client.ServiceVOIPDeviceAddEdit2() # ServiceVOIPDeviceAddEdit2 | device fields

    try:
        # Update Device
        api_response = api_instance.v1_account_accountid_device_deviceid_put(accountid, deviceid, device)
        print("The response of DeviceApi->v1_account_accountid_device_deviceid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->v1_account_accountid_device_deviceid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **deviceid** | **str**| Device ID, 32 alpha numeric | 
 **device** | [**ServiceVOIPDeviceAddEdit2**](ServiceVOIPDeviceAddEdit2.md)| device fields | 

### Return type

[**ServiceDocsDeviceGetSingle**](ServiceDocsDeviceGetSingle.md)

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

# **v1_account_accountid_device_deviceid_reboot_post**
> ServiceDocsDeviceReboot v1_account_accountid_device_deviceid_reboot_post(accountid, deviceid)

Reboot Device

Reboot a device in an account to mitigate malware and improve device performance.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_device_reboot import ServiceDocsDeviceReboot
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
    api_instance = openapi_client.DeviceApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    deviceid = 'deviceid_example' # str | Device ID, 32 alpha numeric

    try:
        # Reboot Device
        api_response = api_instance.v1_account_accountid_device_deviceid_reboot_post(accountid, deviceid)
        print("The response of DeviceApi->v1_account_accountid_device_deviceid_reboot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->v1_account_accountid_device_deviceid_reboot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **deviceid** | **str**| Device ID, 32 alpha numeric | 

### Return type

[**ServiceDocsDeviceReboot**](ServiceDocsDeviceReboot.md)

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

# **v1_account_accountid_device_get**
> ServiceDocsDeviceGetAll v1_account_accountid_device_get(accountid, start_key=start_key, page_size=page_size)

Get Device List

Obtain a list of all devices associated with an account such as fax machines, cell phones, and soft phones.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_device_get_all import ServiceDocsDeviceGetAll
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
    api_instance = openapi_client.DeviceApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    start_key = 'start_key_example' # str | start_key for pagination that was returned as next_start_key from your previous call (optional)
    page_size = 56 # int | number of records to return, range 1 to 50 (optional)

    try:
        # Get Device List
        api_response = api_instance.v1_account_accountid_device_get(accountid, start_key=start_key, page_size=page_size)
        print("The response of DeviceApi->v1_account_accountid_device_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->v1_account_accountid_device_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **start_key** | **str**| start_key for pagination that was returned as next_start_key from your previous call | [optional] 
 **page_size** | **int**| number of records to return, range 1 to 50 | [optional] 

### Return type

[**ServiceDocsDeviceGetAll**](ServiceDocsDeviceGetAll.md)

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

# **v1_account_accountid_device_post**
> ServiceDocsDeviceGetSingle v1_account_accountid_device_post(accountid, device)

Create Device

Connect a new device to an account to enhance communication methods.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_device_get_single import ServiceDocsDeviceGetSingle
from openapi_client.models.service_voip_device_add_edit2 import ServiceVOIPDeviceAddEdit2
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
    api_instance = openapi_client.DeviceApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric
    device = openapi_client.ServiceVOIPDeviceAddEdit2() # ServiceVOIPDeviceAddEdit2 | device fields

    try:
        # Create Device
        api_response = api_instance.v1_account_accountid_device_post(accountid, device)
        print("The response of DeviceApi->v1_account_accountid_device_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->v1_account_accountid_device_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 
 **device** | [**ServiceVOIPDeviceAddEdit2**](ServiceVOIPDeviceAddEdit2.md)| device fields | 

### Return type

[**ServiceDocsDeviceGetSingle**](ServiceDocsDeviceGetSingle.md)

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

# **v1_account_accountid_device_status_get**
> ServiceDocsDeviceStatus v1_account_accountid_device_status_get(accountid)

Get Device Status

Retrieve a device’s status (e.g., registered or not registered) in an account.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.service_docs_device_status import ServiceDocsDeviceStatus
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
    api_instance = openapi_client.DeviceApi(api_client)
    accountid = 'accountid_example' # str | Account ID, 32 alpha numeric

    try:
        # Get Device Status
        api_response = api_instance.v1_account_accountid_device_status_get(accountid)
        print("The response of DeviceApi->v1_account_accountid_device_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->v1_account_accountid_device_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account ID, 32 alpha numeric | 

### Return type

[**ServiceDocsDeviceStatus**](ServiceDocsDeviceStatus.md)

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

