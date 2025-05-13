from fastapi import FastAPI
from gel import create_client
from pydantic import BaseModel

app = FastAPI()

client = create_client()


class Song(BaseModel):
    title: str
    artist: str
    country: str
    eurovision_song_page: str
    youtube_video: str


class EurovisionEdition(BaseModel):
    year: int
    winner: str | None = None
    hostCountry: str
    songs: list[Song]


@app.get("/editions", response_model=list[EurovisionEdition])
async def editions():
    result = client.query("select EurovisionEdition { year, winner, hostCountry }")

    return result


@app.get("/{year}", response_model=EurovisionEdition)
async def edition(year: int):
    result = client.query_single(
        """
        select EurovisionEdition {
            year,
            winner,
            hostCountry,
            songs: { title, artist, country, eurovision_song_page, youtube_video }
        } filter .year = <int16>$year
        """,
        year=year,
    )
    return result
