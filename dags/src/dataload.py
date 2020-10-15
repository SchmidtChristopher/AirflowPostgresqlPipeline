import json
import pathlib
import pandas as pd
import numpy as np
import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook


path = pathlib.Path("~/airflow/dags/src") / "data"


def load_data(username="Schmidt2k"):
    pg_hook = PostgresHook(postgres_conn_id="top_albums")
    filename = username + "_" + str(datetime.date.today()) + ".csv"
    df = pd.read_csv(path / filename, encoding="utf-8", sep="|")

    rank = df["rank"].values.tolist()
    artist_name = df["artist_name"].values.tolist()
    mbid = df["mbid"].fillna("MISSING").values.tolist()
    playcount = df["playcount"].fillna(-1).values.tolist()
    image_url = df["image_url"].fillna("MISSING").values.tolist()
    artist_url = df["artist_url"].fillna("MISSING").values.tolist()

    columns = (rank, artist_name, mbid, playcount, image_url, artist_url)

    insert_query = """INSERT INTO lastFM_topalbums
                    (rank, artist_name, mbid,playcount,
                    image_url, artist_url)
                    VALUES
                    (%s,%s,%s,%s,%s,%s);
    """
    n_rows = len(rank)
    # FIXME double check rows load
    for entry in range(n_rows):
        pg_hook.run(
            insert_query,
            parameters=(
                rank[entry],
                artist_name[entry],
                mbid[entry],
                playcount[entry],
                image_url[entry],
                artist_url[entry],
            ),
        )


if __name__ == "__main__":
    load_data()
