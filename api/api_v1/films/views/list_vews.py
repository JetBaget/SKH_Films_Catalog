from fastapi import (
    APIRouter,
    status,
)

from api.api_v1.films.crud import storage

from schemas.film_info import FilmInfo, FilmInfoCreate


router = APIRouter(
    prefix="/films",
    tags=["Film catalog"],
)


@router.get(
    path="/",
    response_model=list[FilmInfo],
)
def read_films_list() -> list[FilmInfo]:
    return storage.get()


@router.post(
    path="/",
    response_model=FilmInfo,
    status_code=status.HTTP_201_CREATED,
)
def add_film(
    film_info_create: FilmInfoCreate,
):
    storage.create(film_info_create)
    return FilmInfo(
        **film_info_create.model_dump(),
    )
