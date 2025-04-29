from typing import Annotated

from http.client import HTTPException

import uvicorn
from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    status,
    Depends,
)

from schemas.film_info import FilmInfo

FILMS = [
    FilmInfo(
        id=1,
        genre="Fantasy",
        name="Star Wars 1",
        description="Princess Lea and Shubaca action",
        age_restriction=10,
    ),
    FilmInfo(
        id=3,
        genre="Gachi",
        name="Boss of the gym",
        description="The struggle of men in oil for the right to be the best",
        age_restriction=18,
    ),
]

app = FastAPI(title="Film catalog")


@app.get("/")
def hello(request: Request, name: str = "World"):
    docs_url = request.url.replace(
        path="docs",
        query="",
    )
    return {
        "message": f"Hello, {name}!",
        "docs": str(docs_url),
    }


@app.get(path="/films/", response_model=list[FilmInfo])
def read_films_list():
    return FILMS


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


@app.get(
    path="/film_info/{id}/",
    response_model=FilmInfo,
)
def read_film_info(
    film_info: Annotated[
        FilmInfo,
        Depends(get_film_info),
    ],
) -> FilmInfo:
    return film_info


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
    )
