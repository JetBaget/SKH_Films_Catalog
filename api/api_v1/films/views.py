from random import randint

from annotated_types import Len
from typing import Annotated

from fastapi import (
    Depends,
    APIRouter,
    status,
    Form,
)

from .crud import FILMS
from .dependencies import get_film_info

from schemas.film_info import FilmInfo


router = APIRouter(
    prefix="/films",
    tags=["Film catalog"],
)


@router.get(path="/", response_model=list[FilmInfo])
def read_films_list():
    return FILMS


@router.post(
    path="/",
    response_model=FilmInfo,
    status_code=status.HTTP_201_CREATED,
)
def add_film(
    name: Annotated[
        str,
        Len(min_length=3, max_length=20),
        Form(),
    ],
    description: Annotated[
        str,
        Len(min_length=10, max_length=100),
        Form(),
    ],
    genre: Annotated[
        str,
        Len(min_length=3, max_length=20),
        Form(),
    ],
    age_restriction: Annotated[int, Form()] = 10,
):
    return FilmInfo(
        id=randint(1, 100),
        name=name,
        description=description,
        genre=genre,
        age_restriction=age_restriction,
    )


@router.get(
    path="/info/{id}/",
    response_model=FilmInfo,
)
def read_film_info(
    film_info: Annotated[
        FilmInfo,
        Depends(get_film_info),
    ],
) -> FilmInfo:
    return film_info
