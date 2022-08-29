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


class HealthCheckResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Just a string to inform instance is up and running. Make it nullable in hope to get it as pointer in generated model.
    """


    class MetaOapg:
        class properties:
            
            
            class NullableMessage(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, str, ]),
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'NullableMessage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        additional_properties = schemas.AnyTypeSchema
    
    NullableMessage: MetaOapg.properties.NullableMessage

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        NullableMessage: typing.Union[MetaOapg.properties.NullableMessage, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'HealthCheckResult':
        return super().__new__(
            cls,
            *args,
            NullableMessage=NullableMessage,
            _configuration=_configuration,
            **kwargs,
        )
