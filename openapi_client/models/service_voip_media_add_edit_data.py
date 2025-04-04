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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.service_tts import ServiceTTS
from typing import Optional, Set
from typing_extensions import Self

class ServiceVOIPMediaAddEditData(BaseModel):
    """
    ServiceVOIPMediaAddEditData
    """ # noqa: E501
    description: Optional[Annotated[str, Field(strict=True, max_length=128)]] = None
    media_source: Optional[StrictStr] = None
    name: Annotated[str, Field(strict=True, max_length=128)]
    tts: Optional[ServiceTTS] = None
    __properties: ClassVar[List[str]] = ["description", "media_source", "name", "tts"]

    @field_validator('media_source')
    def media_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['upload', 'recording', 'tts']):
            raise ValueError("must be one of enum values ('upload', 'recording', 'tts')")
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
        """Create an instance of ServiceVOIPMediaAddEditData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tts
        if self.tts:
            _dict['tts'] = self.tts.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceVOIPMediaAddEditData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "media_source": obj.get("media_source"),
            "name": obj.get("name"),
            "tts": ServiceTTS.from_dict(obj["tts"]) if obj.get("tts") is not None else None
        })
        return _obj


