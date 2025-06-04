from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel


class FilmInfoBase(BaseModel):
    """
    Базовая модель фильма
    """

    name: str
    genre: str
    age_restriction: int
    description: Annotated[
        str,
        Len(min_length=10, max_length=100),
    ]


class FilmInfoCreate(FilmInfoBase):
    """
    Модель для создания фильма
    """

    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]


class FilmInfo(FilmInfoBase):
    """
    Модель описания фильма
    """

    slug: str


class FilmInfoUpdate(FilmInfoBase):
    """
    Модель для обновления информации о фильме
    """
