import pandas as pd
import requests
import datetime
import credentials as C
import pathlib


def get_topalbums(user="Schmidt2k", rank=5):
    params = {
        "method": "user.gettopalbums",
        "user": user,
        "api_key": C.credentials["key"],
        "limit": rank,  # number of entries to fetch, ordered list ascending.
        "format": "json",
        "period": "7day",
    }

    # Placeholders
    responses = []

    # root url
    url = "http://ws.audioscrobbler.com/2.0/"
    response = requests.get(url, params=params)
    responses.append(response.json())

    if response.status_code == 200:
        rank = []
        artist_name = []
        mbid = []
        playcount = []
        artist_url = []
        image_url = []

        for page in responses:
            for album in page["topalbums"]["album"]:
                rank.append(album["@attr"]["rank"])
                artist_name.append(album["name"])
                mbid.append(album["mbid"])
                playcount.append(album["playcount"])
                artist_url.append(album["url"])
                for size in album["image"]:
                    if size["size"] == "extralarge":
                        image_url.append(size["#text"])

        mydf = pd.DataFrame()
        mydf["rank"] = rank
        mydf["artist_name"] = artist_name
        mydf["mbid"] = mbid
        mydf["playcount"] = playcount
        mydf["image_url"] = image_url
        mydf["artist_url"] = artist_url

        # Export to csv
        name = f"{user}_" + str(datetime.date.today()) + ".csv"
        path = pathlib.Path("~/airflow/dags/src/data")
        mydf.to_csv(path / name, header=True, index=False, sep="|", mode="w")

    else:
        print("Error in API call.")


if __name__ == "__main__":
    get_topalbums()

