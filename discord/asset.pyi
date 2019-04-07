from typing import Any, Optional, Union, FrozenSet, BinaryIO
from typing_extensions import Final
from os import PathLike

VALID_STATIC_FORMATS: Final[FrozenSet[str]]
VALID_AVATAR_FORMATS: Final[FrozenSet[str]]

class Asset:
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    async def save(self, fp: Union[BinaryIO, PathLike[str], str], *, seek_begin: bool = ...) -> int: ...
