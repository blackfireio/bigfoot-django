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

1. Generate fake data:
   
   ```bash
   # Run the following command in the pipenv shell
   python manage.py migrate
   python manage.py generate_fake_data
   ```

1. Run server with `blackfire-python`:

   ```bash
   blackfire-python manage.py runserver
   ```
