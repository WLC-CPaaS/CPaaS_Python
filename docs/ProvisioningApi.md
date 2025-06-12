# openapi_client.ProvisioningApi

All URIs are relative to *http://API_HOSTNAME*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_ap_brand_brand_family_family_get**](ProvisioningApi.md#v1_ap_brand_brand_family_family_get) | **GET** /v1/ap/brand/{brand}/family/{family} | Get Family
[**v1_ap_brand_brand_family_family_model_get**](ProvisioningApi.md#v1_ap_brand_brand_family_family_model_get) | **GET** /v1/ap/brand/{brand}/family/{family}/model | Get Model List
[**v1_ap_brand_brand_family_family_model_model_get**](ProvisioningApi.md#v1_ap_brand_brand_family_family_model_model_get) | **GET** /v1/ap/brand/{brand}/family/{family}/model/{model} | Get Model
[**v1_ap_brand_brand_family_family_model_model_template_get**](ProvisioningApi.md#v1_ap_brand_brand_family_family_model_model_template_get) | **GET** /v1/ap/brand/{brand}/family/{family}/model/{model}/template | Get Template List
[**v1_ap_brand_brand_family_family_model_model_template_template_get**](ProvisioningApi.md#v1_ap_brand_brand_family_family_model_model_template_template_get) | **GET** /v1/ap/brand/{brand}/family/{family}/model/{model}/template/{template} | Get Template
[**v1_ap_brand_brand_family_get**](ProvisioningApi.md#v1_ap_brand_brand_family_get) | **GET** /v1/ap/brand/{brand}/family | Get Family List
[**v1_ap_brand_brand_get**](ProvisioningApi.md#v1_ap_brand_brand_get) | **GET** /v1/ap/brand/{brand} | Get Brand
[**v1_ap_brand_get**](ProvisioningApi.md#v1_ap_brand_get) | **GET** /v1/ap/brand | Get Brand
[**v1_ap_configfile_generate_post**](ProvisioningApi.md#v1_ap_configfile_generate_post) | **POST** /v1/ap/configfile/generate | Generate config file


# **v1_ap_brand_brand_family_family_get**
> ProvisioningDocsDocsFamilyOutputSingle v1_ap_brand_brand_family_family_get(brand, family)

Get Family

Retrieve a family's details by the randomly generated ID.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.provisioning_docs_docs_family_output_single import ProvisioningDocsDocsFamilyOutputSingle
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
    api_instance = openapi_client.ProvisioningApi(api_client)
    brand = 'brand_example' # str | brand
    family = 'family_example' # str | family

    try:
        # Get Family
        api_response = api_instance.v1_ap_brand_brand_family_family_get(brand, family)
        print("The response of ProvisioningApi->v1_ap_brand_brand_family_family_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->v1_ap_brand_brand_family_family_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand** | **str**| brand | 
 **family** | **str**| family | 

### Return type

[**ProvisioningDocsDocsFamilyOutputSingle**](ProvisioningDocsDocsFamilyOutputSingle.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ap_brand_brand_family_family_model_get**
> ProvisioningDocsDocsModelOutput v1_ap_brand_brand_family_family_model_get(brand, family, model_name=model_name, page_size=page_size, start_key=start_key, status=status)

Get Model List

Retrieve a list of all models within a family for a brand (e.g., Yealink and Polycom).

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.provisioning_docs_docs_model_output import ProvisioningDocsDocsModelOutput
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
    api_instance = openapi_client.ProvisioningApi(api_client)
    brand = 'brand_example' # str | brand
    family = 'family_example' # str | family
    model_name = 'model_name_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_key = 'start_key_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Get Model List
        api_response = api_instance.v1_ap_brand_brand_family_family_model_get(brand, family, model_name=model_name, page_size=page_size, start_key=start_key, status=status)
        print("The response of ProvisioningApi->v1_ap_brand_brand_family_family_model_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->v1_ap_brand_brand_family_family_model_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand** | **str**| brand | 
 **family** | **str**| family | 
 **model_name** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_key** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**ProvisioningDocsDocsModelOutput**](ProvisioningDocsDocsModelOutput.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ap_brand_brand_family_family_model_model_get**
> ProvisioningDocsDocsModelOutputSingle v1_ap_brand_brand_family_family_model_model_get(brand, family, model)

Get Model

Retrieve a model's details by the randomly generated ID.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.provisioning_docs_docs_model_output_single import ProvisioningDocsDocsModelOutputSingle
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
    api_instance = openapi_client.ProvisioningApi(api_client)
    brand = 'brand_example' # str | brand
    family = 'family_example' # str | family
    model = 'model_example' # str | model

    try:
        # Get Model
        api_response = api_instance.v1_ap_brand_brand_family_family_model_model_get(brand, family, model)
        print("The response of ProvisioningApi->v1_ap_brand_brand_family_family_model_model_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->v1_ap_brand_brand_family_family_model_model_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand** | **str**| brand | 
 **family** | **str**| family | 
 **model** | **str**| model | 

### Return type

[**ProvisioningDocsDocsModelOutputSingle**](ProvisioningDocsDocsModelOutputSingle.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ap_brand_brand_family_family_model_model_template_get**
> ProvisioningDocsDocsTemplatesOutput v1_ap_brand_brand_family_family_model_model_template_get(brand, family, model, firmware=firmware, page_size=page_size, start_key=start_key, status=status, template_name=template_name)

Get Template List

Retrieve a list of all templates for a model within a brand (e.g., Yealink and Polycom).

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.provisioning_docs_docs_templates_output import ProvisioningDocsDocsTemplatesOutput
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
    api_instance = openapi_client.ProvisioningApi(api_client)
    brand = 'brand_example' # str | brand
    family = 'family_example' # str | family
    model = 'model_example' # str | model
    firmware = 'firmware_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_key = 'start_key_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    template_name = 'template_name_example' # str |  (optional)

    try:
        # Get Template List
        api_response = api_instance.v1_ap_brand_brand_family_family_model_model_template_get(brand, family, model, firmware=firmware, page_size=page_size, start_key=start_key, status=status, template_name=template_name)
        print("The response of ProvisioningApi->v1_ap_brand_brand_family_family_model_model_template_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->v1_ap_brand_brand_family_family_model_model_template_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand** | **str**| brand | 
 **family** | **str**| family | 
 **model** | **str**| model | 
 **firmware** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_key** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **template_name** | **str**|  | [optional] 

### Return type

[**ProvisioningDocsDocsTemplatesOutput**](ProvisioningDocsDocsTemplatesOutput.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ap_brand_brand_family_family_model_model_template_template_get**
> ProvisioningDocsDocsTemplateOutputSingle v1_ap_brand_brand_family_family_model_model_template_template_get(brand, family, model, template)

Get Template

Retrieve details about a template for a model by the randomly generated ID.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.provisioning_docs_docs_template_output_single import ProvisioningDocsDocsTemplateOutputSingle
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
    api_instance = openapi_client.ProvisioningApi(api_client)
    brand = 'brand_example' # str | brand
    family = 'family_example' # str | family
    model = 'model_example' # str | model
    template = 'template_example' # str | template

    try:
        # Get Template
        api_response = api_instance.v1_ap_brand_brand_family_family_model_model_template_template_get(brand, family, model, template)
        print("The response of ProvisioningApi->v1_ap_brand_brand_family_family_model_model_template_template_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->v1_ap_brand_brand_family_family_model_model_template_template_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand** | **str**| brand | 
 **family** | **str**| family | 
 **model** | **str**| model | 
 **template** | **str**| template | 

### Return type

[**ProvisioningDocsDocsTemplateOutputSingle**](ProvisioningDocsDocsTemplateOutputSingle.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ap_brand_brand_family_get**
> ProvisioningDocsDocsFamilyOutput v1_ap_brand_brand_family_get(brand, family_name=family_name, page_size=page_size, start_key=start_key, status=status)

Get Family List

Retrieve a list of all families for a brand (e.g., Yealink and Polycom).

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.provisioning_docs_docs_family_output import ProvisioningDocsDocsFamilyOutput
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
    api_instance = openapi_client.ProvisioningApi(api_client)
    brand = 'brand_example' # str | brand
    family_name = 'family_name_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_key = 'start_key_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Get Family List
        api_response = api_instance.v1_ap_brand_brand_family_get(brand, family_name=family_name, page_size=page_size, start_key=start_key, status=status)
        print("The response of ProvisioningApi->v1_ap_brand_brand_family_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->v1_ap_brand_brand_family_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand** | **str**| brand | 
 **family_name** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_key** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**ProvisioningDocsDocsFamilyOutput**](ProvisioningDocsDocsFamilyOutput.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ap_brand_brand_get**
> ProvisioningDocsDocsBrandOutputSingle v1_ap_brand_brand_get(brand)

Get Brand

Retrieve a brand's details by the randomly generated ID.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.provisioning_docs_docs_brand_output_single import ProvisioningDocsDocsBrandOutputSingle
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
    api_instance = openapi_client.ProvisioningApi(api_client)
    brand = 'brand_example' # str | brand id to retrieve a brand

    try:
        # Get Brand
        api_response = api_instance.v1_ap_brand_brand_get(brand)
        print("The response of ProvisioningApi->v1_ap_brand_brand_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->v1_ap_brand_brand_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand** | **str**| brand id to retrieve a brand | 

### Return type

[**ProvisioningDocsDocsBrandOutputSingle**](ProvisioningDocsDocsBrandOutputSingle.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ap_brand_get**
> ProvisioningDocsDocsBrandsOutput v1_ap_brand_get(brand_name=brand_name, page_size=page_size, start_key=start_key, status=status)

Get Brand

Retrieve a list of all brands (e.g., Yealink and Polycom) by client.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.provisioning_docs_docs_brands_output import ProvisioningDocsDocsBrandsOutput
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
    api_instance = openapi_client.ProvisioningApi(api_client)
    brand_name = 'brand_name_example' # str |  (optional)
    page_size = 56 # int |  (optional)
    start_key = 'start_key_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Get Brand
        api_response = api_instance.v1_ap_brand_get(brand_name=brand_name, page_size=page_size, start_key=start_key, status=status)
        print("The response of ProvisioningApi->v1_ap_brand_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->v1_ap_brand_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_name** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **start_key** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**ProvisioningDocsDocsBrandsOutput**](ProvisioningDocsDocsBrandsOutput.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ap_configfile_generate_post**
> ProvisioningDocsDocsConfigFileOutput v1_ap_configfile_generate_post(params)

Generate config file

Generate a configuration file that includes a list of parameters passed to the specified template_id in the request payload, with populated values returned in the response.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.models_generate_config_file_request import ModelsGenerateConfigFileRequest
from openapi_client.models.provisioning_docs_docs_config_file_output import ProvisioningDocsDocsConfigFileOutput
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
    api_instance = openapi_client.ProvisioningApi(api_client)
    params = openapi_client.ModelsGenerateConfigFileRequest() # ModelsGenerateConfigFileRequest | body params to generate config file

    try:
        # Generate config file
        api_response = api_instance.v1_ap_configfile_generate_post(params)
        print("The response of ProvisioningApi->v1_ap_configfile_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->v1_ap_configfile_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**ModelsGenerateConfigFileRequest**](ModelsGenerateConfigFileRequest.md)| body params to generate config file | 

### Return type

[**ProvisioningDocsDocsConfigFileOutput**](ProvisioningDocsDocsConfigFileOutput.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

