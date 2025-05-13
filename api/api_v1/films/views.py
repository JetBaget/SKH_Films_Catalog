from random import randint

from typing import Annotated

from fastapi import (
    Depends,
    APIRouter,
    status,
)

from .crud import FILMS
from .dependencies import get_film_info

from schemas.film_info import FilmInfo, FilmInfoCreate


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
    film_info_create: FilmInfoCreate,
):
    return FilmInfo(
        **film_info_create.model_dump(),
    )


@router.get(
    path="/info/{slug}/",
    response_model=FilmInfo,
)
def read_film_info(
    film_info: Annotated[
        FilmInfo,
        Depends(get_film_info),
    ],
) -> FilmInfo:
    return film_info
