from typing import Annotated

from fastapi import (
    Depends,
    APIRouter,
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
