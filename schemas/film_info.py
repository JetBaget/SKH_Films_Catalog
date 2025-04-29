from pydantic import BaseModel


class FilmInfoBase(BaseModel):
    id: int
    name: str
    description: str
    genre: str
    age_restriction: int


class FilmInfo(FilmInfoBase):
    """
    Модель описания фильма
    """
