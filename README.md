# Airflow Data Pipeline

Example of how a local ETL pipeline can be set up using <a href="https://airflow.incubator.apache.org/">Airflow</a>. The Airflow DAG is set up to query the <a href="https://www.last.fm/">LastFM</a> API daily, process the json data, and store it in a local <a href="https://www.postgresql.org/">PostgreSQL</a> database.


Requirements

<a href="https://airflow.incubator.apache.org/">Airflow</a>

<a href="https://www.python.org/">Python 3.8.5</a>

<a href="https://www.postgresql.org/">PostgreSQL</a>

<a href="http://initd.org/psycopg/">psycopg</a>

<a href="https://www.sqlalchemy.org/">SQLAlchemy</a>

For requirements:
pip install -r requirements.t

