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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.service_metaflow_pattern import ServiceMetaflowPattern
from typing import Optional, Set
from typing_extensions import Self

class ServiceVOIPMetaflowAddData(BaseModel):
    """
    ServiceVOIPMetaflowAddData
    """ # noqa: E501
    binding_digit: Optional[StrictStr] = None
    numbers: Optional[Dict[str, ServiceMetaflowPattern]] = None
    patterns: Optional[Dict[str, ServiceMetaflowPattern]] = None
    __properties: ClassVar[List[str]] = ["binding_digit", "numbers", "patterns"]

    @field_validator('binding_digit')
    def binding_digit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '*', '#']):
            raise ValueError("must be one of enum values ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '*', '#')")
        return value

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
        """Create an instance of ServiceVOIPMetaflowAddData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in numbers (dict)
        _field_dict = {}
        if self.numbers:
            for _key_numbers in self.numbers:
                if self.numbers[_key_numbers]:
                    _field_dict[_key_numbers] = self.numbers[_key_numbers].to_dict()
            _dict['numbers'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in patterns (dict)
        _field_dict = {}
        if self.patterns:
            for _key_patterns in self.patterns:
                if self.patterns[_key_patterns]:
                    _field_dict[_key_patterns] = self.patterns[_key_patterns].to_dict()
            _dict['patterns'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceVOIPMetaflowAddData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "binding_digit": obj.get("binding_digit"),
            "numbers": dict(
                (_k, ServiceMetaflowPattern.from_dict(_v))
                for _k, _v in obj["numbers"].items()
            )
            if obj.get("numbers") is not None
            else None,
            "patterns": dict(
                (_k, ServiceMetaflowPattern.from_dict(_v))
                for _k, _v in obj["patterns"].items()
            )
            if obj.get("patterns") is not None
            else None
        })
        return _obj


