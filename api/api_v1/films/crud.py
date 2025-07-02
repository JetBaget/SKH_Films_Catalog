from pathlib import Path

import pydantic_core
from pydantic import BaseModel

from schemas.film_info import (
    FilmInfo,
    FilmInfoCreate,
    FilmInfoUpdate,
    FilmInfoPartialUpdate,
)

JSON_DATA_PATH = "data.json"


class FilmsStorage(BaseModel):
    slug_to_film: dict[str, FilmInfo] = {}

    def load_from_json(self):
        p = Path(JSON_DATA_PATH)
        p.touch(exist_ok=True)
        json_data = p.read_text()
        if json_data:
            try:
                data = self.model_validate_json(json_data)
                self.slug_to_film = data.slug_to_film
            except pydantic_core.ValidationError as err:
                print(f"Pydantic error: {err}")

    def save_to_json(self):
        data = self.model_dump_json()
        p = Path(JSON_DATA_PATH)
        p.write_text(data)

    def get(self) -> list[FilmInfo]:
        return list(self.slug_to_film.values())

    def get_by_slug(self, slug) -> FilmInfo | None:
        return self.slug_to_film.get(slug)

    def create(self, film_info_in: FilmInfoCreate) -> FilmInfo:
        film_info = FilmInfo(
            **film_info_in.model_dump(),
        )
        self.slug_to_film[film_info.slug] = film_info
        self.save_to_json()
        return film_info

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_film.pop(slug, None)
        self.save_to_json()

    def delete(self, film_info: FilmInfo) -> None:
        self.delete_by_slug(slug=film_info.slug)
        self.save_to_json()

    def update(
        self,
        film_info: FilmInfo,
        film_info_in: FilmInfoUpdate,
    ) -> FilmInfo:
        for field_name, value in film_info_in:
            setattr(film_info, field_name, value)
        self.save_to_json()
        return film_info

    def update_partial(
        self,
        film_info: FilmInfo,
        film_info_in: FilmInfoPartialUpdate,
    ) -> FilmInfo:
        for field_name, value in film_info_in.model_dump(exclude_unset=True).items():
            setattr(film_info, field_name, value)
        self.save_to_json()
        return film_info


storage = FilmsStorage()
storage.load_from_json()

storage.create(
    FilmInfoCreate(
        slug="sw1",
        genre="Fantasy",
        name="Star Wars 1",
        description="Princess Lea and Shubaca action",
        age_restriction=10,
    ),
)

storage.create(
    FilmInfoCreate(
        slug="gachi",
        genre="Gachi",
        name="Boss of the gym",
        description="The struggle of men in oil for the right to be the best",
        age_restriction=18,
    ),
)
