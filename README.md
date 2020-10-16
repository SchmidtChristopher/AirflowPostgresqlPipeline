# AirflowPostgresqlPipeline
Local example of an Airflow pipeline using Postgresql

See associated Medium blog post <url>

1. Set up a new virtual environment along with the dependencies, requirements.txt

2. Create a credentials file, 'touch ~/airflow/dags/src/credentials.py'
    Containing:
    credentials = {'user': 'API_USR', 'key': 'API KEY'}
    credentials_sql = {'user': 'POSTGRES_USER', 'password': 'POSTGRES_PASSWORD'}

3. Create a database and table: 'python ~/airflow/dags/src/makeTable.py'

4. Initialize airflow, 'airflow init'
5. Start the airflow webserver, 'airflow webserver -p 8080'
6. go to localhost:8080 and navigate Airflow set up as per ~/airflow/dags/dagdefinition.py
