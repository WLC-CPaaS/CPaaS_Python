# coding: utf-8

"""
    White Label Communications CPaas API Documentation

    A CPaaS platform API

    The version of the OpenAPI document: 1.1
    Contact: support@whitelabelcomm.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.service_call_queue_output_short import ServiceCallQueueOutputShort
from typing import Optional, Set
from typing_extensions import Self

class ServiceDocsCallQueueGetAll(BaseModel):
    """
    ServiceDocsCallQueueGetAll
    """ # noqa: E501
    data: Optional[List[ServiceCallQueueOutputShort]] = None
    next_start_key: Optional[StrictStr] = Field(default=None, description="List Pagination: Used to get the next page of results. Will not exist if this is the last page.")
    page_size: Optional[StrictInt] = Field(default=None, description="List Pagination: The number of results returned in this page")
    request_id: Optional[StrictStr] = Field(default=None, description="Unique id for each request")
    start_key: Optional[StrictStr] = Field(default=None, description="List Pagination: Code for paged results")
    status_code: Optional[StrictInt] = Field(default=None, description="HTTP response status code")
    __properties: ClassVar[List[str]] = ["data", "next_start_key", "page_size", "request_id", "start_key", "status_code"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ServiceDocsCallQueueGetAll from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceDocsCallQueueGetAll from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [ServiceCallQueueOutputShort.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "next_start_key": obj.get("next_start_key"),
            "page_size": obj.get("page_size"),
            "request_id": obj.get("request_id"),
            "start_key": obj.get("start_key"),
            "status_code": obj.get("status_code")
        })
        return _obj


