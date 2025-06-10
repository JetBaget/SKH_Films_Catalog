from typing import Annotated

from fastapi import (
    Depends,
    APIRouter,
    status,
)

from api.api_v1.films.crud import storage
from api.api_v1.films.dependencies import get_film

from schemas.film_info import (
    FilmInfo,
    FilmInfoUpdate,
    FilmInfoPartialUpdate,
)


router = APIRouter(
    prefix="/{slug}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Film not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Film slug not found"},
                },
            },
        },
    },
)


FilmInfoBySlug = Annotated[
    FilmInfo,
    Depends(get_film),
]


@router.get(
    path="/",
    response_model=FilmInfo,
)
def read_film(
    film_info: Annotated[
        FilmInfo,
        Depends(get_film),
    ],
) -> FilmInfo:
    return film_info


@router.delete(
    path="/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_film(
    film_info: FilmInfoBySlug,
) -> None:
    storage.delete(film_info)


@router.put(
    path="/",
    status_code=status.HTTP_200_OK,
)
def update_film(
    film_info: FilmInfoBySlug,
    film_info_in: FilmInfoUpdate,
) -> None:
    storage.update(
        film_info=film_info,
        film_info_in=film_info_in,
    )


@router.patch(
    path="/",
    response_model=FilmInfo,
    status_code=status.HTTP_200_OK,
)
def update_partial_film(
    film_info: FilmInfoBySlug,
    film_info_in: FilmInfoPartialUpdate,
) -> FilmInfo:
    storage.update_partial(
        film_info=film_info,
        film_info_in=film_info_in,
    )
    return film_info
