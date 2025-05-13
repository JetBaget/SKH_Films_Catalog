from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel


class FilmInfoBase(BaseModel):
    name: str
    description: str
    genre: str
    age_restriction: int


class FilmInfoCreate(FilmInfoBase):
    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]
    description: Annotated[
        str,
        Len(min_length=10, max_length=25),
    ]


class FilmInfo(FilmInfoBase):
    """
    Модель описания фильма
    """

    slug: str
