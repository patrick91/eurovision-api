import json
from pathlib import Path

from gel import create_client

here = Path(__file__).parent


def import_data() -> None:
    data = json.loads((here / "data/2025.json").read_text())

    client = create_client()

    # delete all existing data
    client.query("delete EurovisionEdition")
    client.query("delete Song")
    client.query("delete Semifinal")

    # create the eurovision edition with all songs in a single transaction
    client.query(
        """
        with
            songs := (
                for song in json_array_unpack(<json>$songs) union (
                    insert Song {
                        title := <str>song['song'],
                        artist := <str>song['artist'],
                        country := <str>song['country'],
                        eurovision_song_page := <str>song['eurovision_song_page'],
                        youtube_video := <str>song['youtube_video']
                    }
                )
            )
        insert EurovisionEdition {
            year := <int16>$year,
            hostCountry := <str>$hostCountry,
            songs := songs
        }
        """,
        year=data["year"],
        hostCountry=data["host_country"],
        songs=json.dumps(data["participating_countries"]),
    )


if __name__ == "__main__":
    import_data()
