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
from openapi_client.models.menu_output_detail_media import MenuOutputDetailMedia
from typing import Optional, Set
from typing_extensions import Self

class MenuOutputDetailData(BaseModel):
    """
    MenuOutputDetailData
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID of the menu")
    media: Optional[MenuOutputDetailMedia] = Field(default=None, description="The media (prompt) parameters")
    name: Optional[StrictStr] = Field(default=None, description="A friendly name for the menu")
    timeout: Optional[StrictInt] = Field(default=None, description="The amount of time (in milliseconds) to wait for the caller to begin entering digits")
    __properties: ClassVar[List[str]] = ["id", "media", "name", "timeout"]

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
        """Create an instance of MenuOutputDetailData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of media
        if self.media:
            _dict['media'] = self.media.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MenuOutputDetailData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "media": MenuOutputDetailMedia.from_dict(obj["media"]) if obj.get("media") is not None else None,
            "name": obj.get("name"),
            "timeout": obj.get("timeout")
        })
        return _obj


