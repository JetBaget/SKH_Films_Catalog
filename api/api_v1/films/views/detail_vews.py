from typing import Annotated

from fastapi import (
    Depends,
    APIRouter,
    status,
)

from api.api_v1.films.crud import storage
from api.api_v1.films.dependencies import get_film

from schemas.film_info import FilmInfo


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
    film_info: Annotated[
        FilmInfo,
        Depends(get_film),
    ],
) -> None:
    storage.delete(film_info)
