from fastapi import (
    status,
    HTTPException,
)

from .crud import FILMS

from schemas.film_info import FilmInfo


def get_film_info(film_id: int) -> FilmInfo:
    film_info: FilmInfo | None = next(
        (film for film in FILMS if film.id == film_id),
        None,
    )
    if film_info:
        return film_info
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Film with id={film_id!r} not found",
    )
