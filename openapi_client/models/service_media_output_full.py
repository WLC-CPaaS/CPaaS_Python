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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.service_tts import ServiceTTS
from typing import Optional, Set
from typing_extensions import Self

class ServiceMediaOutputFull(BaseModel):
    """
    ServiceMediaOutputFull
    """ # noqa: E501
    content_length: Optional[StrictInt] = None
    content_type: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    media_source: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    streamable: Optional[StrictBool] = None
    tts: Optional[ServiceTTS] = None
    __properties: ClassVar[List[str]] = ["content_length", "content_type", "description", "id", "language", "media_source", "name", "streamable", "tts"]

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
        """Create an instance of ServiceMediaOutputFull from a JSON string"""
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
        """Create an instance of ServiceMediaOutputFull from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content_length": obj.get("content_length"),
            "content_type": obj.get("content_type"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "language": obj.get("language"),
            "media_source": obj.get("media_source"),
            "name": obj.get("name"),
            "streamable": obj.get("streamable"),
            "tts": ServiceTTS.from_dict(obj["tts"]) if obj.get("tts") is not None else None
        })
        return _obj


