import psycopg2
import credentials as C
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

user = C.credentials_sql["user"]
password = C.credentials_sql["password"]


def make_database():
    """
    Comment
    """

    user = C.credentials_sql["user"]
    dbname = "Topartists"
    password = C.credentials_sql["password"]

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@localhost/{dbname}"
    )

    if not database_exists(engine.url):
        create_database(engine.url)

    conn = psycopg2.connect(database=dbname, user=user, password=password)

    curr = conn.cursor()

    table = "lastFM_topalbums"
    create_table = f"""CREATE TABLE IF NOT EXISTS {table}
                    (
                        rank INTEGER,
                        artist_name VARCHAR,
                        mbid VARCHAR,
                        playcount INTEGER,
                        image_url VARCHAR,
                        artist_url VARCHAR
                    )
                    """

    curr.execute(create_table)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    make_database()
