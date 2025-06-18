from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DrinkSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DRINK_SIZE_UNSPECIFIED: _ClassVar[DrinkSize]
    DRINK_SIZE_SMALL: _ClassVar[DrinkSize]
    DRINK_SIZE_MEDIUM: _ClassVar[DrinkSize]
    DRINK_SIZE_LARGE: _ClassVar[DrinkSize]
DRINK_SIZE_UNSPECIFIED: DrinkSize
DRINK_SIZE_SMALL: DrinkSize
DRINK_SIZE_MEDIUM: DrinkSize
DRINK_SIZE_LARGE: DrinkSize

class DrinkItem(_message.Message):
    __slots__ = ("id", "name", "description", "size", "price")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    size: DrinkSize
    price: float
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., size: _Optional[_Union[DrinkSize, str]] = ..., price: _Optional[float] = ...) -> None: ...

class AddDrinkRequest(_message.Message):
    __slots__ = ("name", "description", "base_price", "available")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BASE_PRICE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    base_price: float
    available: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., base_price: _Optional[float] = ..., available: bool = ...) -> None: ...

class AddDrinkResponse(_message.Message):
    __slots__ = ("drink", "success", "message")
    DRINK_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    drink: DrinkItem
    success: bool
    message: str
    def __init__(self, drink: _Optional[_Union[DrinkItem, _Mapping]] = ..., success: bool = ..., message: _Optional[str] = ...) -> None: ...

class GetMenuRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMenuResponse(_message.Message):
    __slots__ = ("drinks", "message")
    DRINKS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    drinks: _containers.RepeatedCompositeFieldContainer[DrinkItem]
    message: str
    def __init__(self, drinks: _Optional[_Iterable[_Union[DrinkItem, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...
