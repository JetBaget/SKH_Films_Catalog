from fastapi import (
    status,
    HTTPException,
)

from .crud import storage

from schemas.film_info import FilmInfo


def get_film(slug: str) -> FilmInfo:
    film_info: FilmInfo | None = storage.get_by_slug(slug=slug)
    if film_info:
        return film_info
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Film with slug={slug!r} not found",
    )
