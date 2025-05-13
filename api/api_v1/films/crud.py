from schemas.film_info import FilmInfo


FILMS = [
    FilmInfo(
        slug="sw1",
        genre="Fantasy",
        name="Star Wars 1",
        description="Princess Lea and Shubaca action",
        age_restriction=10,
    ),
    FilmInfo(
        slug="gachi",
        genre="Gachi",
        name="Boss of the gym",
        description="The struggle of men in oil for the right to be the best",
        age_restriction=18,
    ),
]
