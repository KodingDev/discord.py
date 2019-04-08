import datetime

from .colour import Colour
from .types import RawEmbedDict, EmbedFooterData, EmbedImageData, EmbedVideoData, EmbedProviderData, EmbedAuthorData, EmbedFieldData

from typing import Any, Union, Dict, List, ClassVar, TypeVar, Type
from mypy_extensions import TypedDict
from typing_extensions import Final

class _EmptyEmbed:
    def __bool__(self) -> bool: ...

    def __repr__(self) -> str: ...

    def __len__(self) -> int: ...

EmptyEmbed: Final[_EmptyEmbed] = ...

class EmbedProxy:
    def __init__(self, layer: Dict[str, Any]) -> None: ...

    def __len__(self) -> int: ...

    def __repr__(self) -> str: ...

    def __getattr__(self, attr: str) -> _EmptyEmbed: ...

_E = TypeVar('_E', bound=Embed)

class Embed:
    title: Union[str, _EmptyEmbed]
    type: str
    description: Union[str, _EmptyEmbed]
    url: Union[str, _EmptyEmbed]
    colour: Union[int, Colour, _EmptyEmbed]
    color: Union[int, Colour, _EmptyEmbed]
    timestamp: Union[datetime.datetime, _EmptyEmbed]

    Empty: ClassVar[_EmptyEmbed]

    def __init__(self, *, color: Union[int, Colour, _EmptyEmbed] = ..., colour: Union[int, Colour, _EmptyEmbed] = ...,
                 title: Union[str, _EmptyEmbed] = ..., type: str = ..., url: Union[str, _EmptyEmbed] = ...,
                 description: Union[str, _EmptyEmbed] = ..., timestamp: Union[datetime.datetime, _EmptyEmbed] = ...) -> None: ...

    @classmethod
    def from_dict(cls: Type[_E], data: RawEmbedDict) -> _E: ...

    def copy(self) -> Embed: ...

    def __len__(self) -> int: ...

    @property
    def footer(self) -> EmbedFooterData: ...

    def set_footer(self, *, text: Union[str, _EmptyEmbed] = ..., icon_url: Union[str, _EmptyEmbed] = ...) -> _E: ...

    @property
    def image(self) -> EmbedImageData: ...

    def set_image(self, *, url: str) -> _E: ...

    @property
    def thumbnail(self) -> EmbedImageData: ...

    def set_thumbnail(self, *, url: str) -> _E: ...

    @property
    def video(self) -> EmbedVideoData: ...

    @property
    def provider(self) -> EmbedProviderData: ...

    @property
    def author(self) -> EmbedAuthorData: ...

    def set_author(self, *, name: str, url: Union[str, _EmptyEmbed] = ..., icon_url: Union[str, _EmptyEmbed] = ...) -> _E: ...

    @property
    def fields(self) -> List[EmbedFieldData]: ...

    def add_field(self, *, name: str, value: str, inline: bool = ...) -> _E: ...

    def clear_fields(self) -> None: ...

    def remove_field(self, index: int) -> None: ...

    def set_field_at(self, index: int, *, name: str, value: str, inline: bool = ...) -> _E: ...

    def to_dict(self) -> RawEmbedDict: ...
