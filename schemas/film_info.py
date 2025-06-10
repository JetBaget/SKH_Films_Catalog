from typing import Annotated

from annotated_types import Len, MaxLen
from pydantic import BaseModel


FilmDescriptionString = Annotated[
    str,
    Len(max_length=100),
]

FilmSlugString = Annotated[
    str,
    Len(min_length=3, max_length=10),
]


class FilmInfoBase(BaseModel):
    """
    Базовая модель фильма
    """

    name: str
    genre: str
    age_restriction: int
    description: FilmDescriptionString


class FilmInfoCreate(FilmInfoBase):
    """
    Модель для создания фильма
    """

    slug: FilmSlugString


class FilmInfo(FilmInfoBase):
    """
    Модель описания фильма
    """

    slug: str


class FilmInfoUpdate(FilmInfoBase):
    """
    Модель для обновления информации о фильме
    """


class FilmInfoPartialUpdate(FilmInfoBase):
    """
    Модель для частичного обновления информации о фильме
    """

    name: str | None = None
    genre: str | None = None
    age_restriction: int | None = None
    description: FilmDescriptionString | None = None
