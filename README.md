# BigFoot Django project

## Installation

Tested only with Python 3.9.

1. Install requirements using `pipenv`:

   ```bash
   pipenv install
   ```

1. Start the PostGreSQL container:

   ```bash
   docker-compose up -d
   ```

2. `pyscopg2` library requires PostgreSQL to be installed on the system.
   (E.x: you might get `pg_config executable not found` errors during installation)

   Make sure PostgreSQL is installed on the host:

   ```
   > brew install postgresql           # MacOS
   > sudo apt-get install postgresql   # Ubuntu
   ```

3. The database user/name are set to `bigfoot` by default. So, you might
   need to run:
   
   ```
   > sudo -u postgres psql
   postgres> createdb bigfoot && createuser -s bigfoot
   ```


4. Generate fake data:
   
   ```bash
   pipenv run python manage.py migrate
   pipenv run python manage.py generate_fake_data
   ```

5. Run server with `blackfire-python`:

   ```bash
   blackfire-python manage.py runserver
   ```
