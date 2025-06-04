from pydantic import BaseModel

from schemas.film_info import FilmInfo, FilmInfoCreate


class FilmsStorage(BaseModel):
    slug_to_film: dict[str, FilmInfo] = {}

    def get(self) -> list[FilmInfo]:
        return list(self.slug_to_film.values())

    def get_by_slug(self, slug) -> FilmInfo | None:
        return self.slug_to_film.get(slug)

    def create(self, film_info_in: FilmInfoCreate) -> FilmInfo:
        film_info = FilmInfo(
            **film_info_in.model_dump(),
        )
        self.slug_to_film[film_info.slug] = film_info
        return film_info

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_film.pop(slug, None)

    def delete(self, film_info: FilmInfo) -> None:
        self.delete_by_slug(slug=film_info.slug)


storage = FilmsStorage()

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
