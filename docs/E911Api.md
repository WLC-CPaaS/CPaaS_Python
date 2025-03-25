# openapi_client.E911Api

All URIs are relative to *http://api.cpaaslabs.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_e911_get**](E911Api.md#v1_e911_get) | **GET** /v1/e911 | Get E911 List
[**v1_e911_location_location_id_activate_put**](E911Api.md#v1_e911_location_location_id_activate_put) | **PUT** /v1/e911/location/{locationID}/activate | Activate E911 Location
[**v1_e911_location_location_id_delete**](E911Api.md#v1_e911_location_location_id_delete) | **DELETE** /v1/e911/location/{locationID} | Delete E911 Location
[**v1_e911_location_validate_put**](E911Api.md#v1_e911_location_validate_put) | **PUT** /v1/e911/location/validate | Validate a Location
[**v1_e911_phone_number_delete**](E911Api.md#v1_e911_phone_number_delete) | **DELETE** /v1/e911/{phoneNumber} | Delete E911 Phone Number
[**v1_e911_phone_number_location_active_get**](E911Api.md#v1_e911_phone_number_location_active_get) | **GET** /v1/e911/{phoneNumber}/location/active | Get Actvie Location for a Phone Number
[**v1_e911_phone_number_location_get**](E911Api.md#v1_e911_phone_number_location_get) | **GET** /v1/e911/{phoneNumber}/location | Get Location List for Phone Number
[**v1_e911_post**](E911Api.md#v1_e911_post) | **POST** /v1/e911 | Create an E911 Location


# **v1_e911_get**
> ServiceDocE911URIsApiOutput v1_e911_get()

Get E911 List

Obtain e911 URIs associated with the provided account ID.

### Example


```python
import openapi_client
from openapi_client.models.service_doc_e911_uris_api_output import ServiceDocE911URIsApiOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.E911Api(api_client)

    try:
        # Get E911 List
        api_response = api_instance.v1_e911_get()
        print("The response of E911Api->v1_e911_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E911Api->v1_e911_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceDocE911URIsApiOutput**](ServiceDocE911URIsApiOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with e911 URIs |  -  |
**403** | Authorization failed or root account not allowed |  -  |
**500** | Internal server error, including environment credential issues, HTTP request failures, or XML unmarshaling errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_e911_location_location_id_activate_put**
> ServiceDocE911ActiveLocationOutput v1_e911_location_location_id_activate_put(location_id)

Activate E911 Location

Edit the provision location.

### Example


```python
import openapi_client
from openapi_client.models.service_doc_e911_active_location_output import ServiceDocE911ActiveLocationOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.E911Api(api_client)
    location_id = 'location_id_example' # str | Location ID

    try:
        # Activate E911 Location
        api_response = api_instance.v1_e911_location_location_id_activate_put(location_id)
        print("The response of E911Api->v1_e911_location_location_id_activate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E911Api->v1_e911_location_location_id_activate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Location ID | 

### Return type

[**ServiceDocE911ActiveLocationOutput**](ServiceDocE911ActiveLocationOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with location activate status |  -  |
**403** | Authorization failed or root account not allowed |  -  |
**500** | Internal server error, including environment credential issues, HTTP request failures, or XML unmarshaling errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_e911_location_location_id_delete**
> ServiceDocE911RemoveLocationOutput v1_e911_location_location_id_delete(location_id)

Delete E911 Location

Remove the location.

### Example


```python
import openapi_client
from openapi_client.models.service_doc_e911_remove_location_output import ServiceDocE911RemoveLocationOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.E911Api(api_client)
    location_id = 'location_id_example' # str | Location ID

    try:
        # Delete E911 Location
        api_response = api_instance.v1_e911_location_location_id_delete(location_id)
        print("The response of E911Api->v1_e911_location_location_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E911Api->v1_e911_location_location_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Location ID | 

### Return type

[**ServiceDocE911RemoveLocationOutput**](ServiceDocE911RemoveLocationOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with location remove status |  -  |
**403** | Authorization failed or root account not allowed |  -  |
**500** | Internal server error, including environment credential issues, HTTP request failures, or XML unmarshaling errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_e911_location_validate_put**
> ServiceDocE911ValidateLocationOutput v1_e911_location_validate_put(req_body)

Validate a Location

Validate the location details.

### Example


```python
import openapi_client
from openapi_client.models.service_doc_e911_validate_location_output import ServiceDocE911ValidateLocationOutput
from openapi_client.models.service_e911_validate_location_input import ServiceE911ValidateLocationInput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.E911Api(api_client)
    req_body = openapi_client.ServiceE911ValidateLocationInput() # ServiceE911ValidateLocationInput | location details

    try:
        # Validate a Location
        api_response = api_instance.v1_e911_location_validate_put(req_body)
        print("The response of E911Api->v1_e911_location_validate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E911Api->v1_e911_location_validate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_body** | [**ServiceE911ValidateLocationInput**](ServiceE911ValidateLocationInput.md)| location details | 

### Return type

[**ServiceDocE911ValidateLocationOutput**](ServiceDocE911ValidateLocationOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with location details |  -  |
**403** | Authorization failed or root account not allowed |  -  |
**500** | Internal server error, including environment credential issues, HTTP request failures, or XML unmarshaling errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_e911_phone_number_delete**
> ServiceDocE911RemoveURIApiOutput v1_e911_phone_number_delete(phone_number)

Delete E911 Phone Number

Delete the e911 URI connected with the account URI.

### Example


```python
import openapi_client
from openapi_client.models.service_doc_e911_remove_uri_api_output import ServiceDocE911RemoveURIApiOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.E911Api(api_client)
    phone_number = 'phone_number_example' # str | Phone Number

    try:
        # Delete E911 Phone Number
        api_response = api_instance.v1_e911_phone_number_delete(phone_number)
        print("The response of E911Api->v1_e911_phone_number_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E911Api->v1_e911_phone_number_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| Phone Number | 

### Return type

[**ServiceDocE911RemoveURIApiOutput**](ServiceDocE911RemoveURIApiOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | Authorization failed or root account not allowed |  -  |
**500** | Internal server error, including environment credential issues, HTTP request failures, or XML unmarshaling errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_e911_phone_number_location_active_get**
> ServiceDocE911ActiveLocationURIApiOutput v1_e911_phone_number_location_active_get(phone_number)

Get Actvie Location for a Phone Number

Get the e911 location connected with the URI.

### Example


```python
import openapi_client
from openapi_client.models.service_doc_e911_active_location_uri_api_output import ServiceDocE911ActiveLocationURIApiOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.E911Api(api_client)
    phone_number = 'phone_number_example' # str | Phone Number

    try:
        # Get Actvie Location for a Phone Number
        api_response = api_instance.v1_e911_phone_number_location_active_get(phone_number)
        print("The response of E911Api->v1_e911_phone_number_location_active_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E911Api->v1_e911_phone_number_location_active_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| Phone Number | 

### Return type

[**ServiceDocE911ActiveLocationURIApiOutput**](ServiceDocE911ActiveLocationURIApiOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with e911 Active Location URI |  -  |
**403** | Authorization failed or root account not allowed |  -  |
**500** | Internal server error, including environment credential issues, HTTP request failures, or XML unmarshaling errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_e911_phone_number_location_get**
> ServiceDocE911LocationsURIApiOutput v1_e911_phone_number_location_get(phone_number)

Get Location List for Phone Number

Access a list of the e911 locations associated with the provided URI.

### Example


```python
import openapi_client
from openapi_client.models.service_doc_e911_locations_uri_api_output import ServiceDocE911LocationsURIApiOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.E911Api(api_client)
    phone_number = 'phone_number_example' # str | Phone Number

    try:
        # Get Location List for Phone Number
        api_response = api_instance.v1_e911_phone_number_location_get(phone_number)
        print("The response of E911Api->v1_e911_phone_number_location_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E911Api->v1_e911_phone_number_location_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| Phone Number | 

### Return type

[**ServiceDocE911LocationsURIApiOutput**](ServiceDocE911LocationsURIApiOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with e911 Locations URI |  -  |
**403** | Authorization failed or root account not allowed |  -  |
**500** | Internal server error, including environment credential issues, HTTP request failures, or XML unmarshaling errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_e911_post**
> ServiceDocE911AddLocationOutput v1_e911_post(req_body)

Create an E911 Location

Enter new location details.

### Example


```python
import openapi_client
from openapi_client.models.service_doc_e911_add_location_output import ServiceDocE911AddLocationOutput
from openapi_client.models.service_e911_add_location_input import ServiceE911AddLocationInput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.cpaaslabs.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.cpaaslabs.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.E911Api(api_client)
    req_body = openapi_client.ServiceE911AddLocationInput() # ServiceE911AddLocationInput | location details

    try:
        # Create an E911 Location
        api_response = api_instance.v1_e911_post(req_body)
        print("The response of E911Api->v1_e911_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E911Api->v1_e911_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_body** | [**ServiceE911AddLocationInput**](ServiceE911AddLocationInput.md)| location details | 

### Return type

[**ServiceDocE911AddLocationOutput**](ServiceDocE911AddLocationOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with location details |  -  |
**403** | Authorization failed or root account not allowed |  -  |
**500** | Internal server error, including environment credential issues, HTTP request failures, or XML unmarshaling errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

