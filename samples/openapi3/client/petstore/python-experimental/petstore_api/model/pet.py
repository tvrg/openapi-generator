# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401
import uuid  # noqa: F401

from petstore_api import schemas  # noqa: F401


class Pet(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Pet object that needs to be added to the store
    """


    class MetaOapg:
        required = {
            "photoUrls",
            "name",
        }
        class properties:
            id = schemas.Int64Schema
        
            @classmethod
            @property
            def category(cls) -> typing.Type['Category']:
                return Category
            name = schemas.StrSchema
            
            
            class photoUrls(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'photoUrls':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
            
                    @classmethod
                    @property
                    def items(cls) -> typing.Type['Tag']:
                        return Tag
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Tag'], typing.List['Tag']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i) -> 'items':
                    return super().__getitem__(i)
            
            
            class status(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        "available": "AVAILABLE",
                        "pending": "PENDING",
                        "sold": "SOLD",
                    }
                ),
                schemas.StrSchema
            ):
                
                @classmethod
                @property
                def AVAILABLE(cls):
                    return cls("available")
                
                @classmethod
                @property
                def PENDING(cls):
                    return cls("pending")
                
                @classmethod
                @property
                def SOLD(cls):
                    return cls("sold")
        additional_properties = schemas.AnyTypeSchema
    
    photoUrls: MetaOapg.properties.photoUrls
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    category: 'Category'
    tags: MetaOapg.properties.tags
    status: MetaOapg.properties.status

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        photoUrls: typing.Union[MetaOapg.properties.photoUrls, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, int, schemas.Unset] = schemas.unset,
        category: typing.Union['Category', schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'Pet':
        return super().__new__(
            cls,
            *args,
            photoUrls=photoUrls,
            name=name,
            id=id,
            category=category,
            tags=tags,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.category import Category
from petstore_api.model.tag import Tag
