# bigfoot_django

## Installation

Tested only with Python 3.9.

1) Install requirements:
   `pip install -r requirements.txt`
2) Generate fake data:
   `python manage.py makemigrations bigfoot`
   `python manage.py migrate bigfoot`
   `python manage.py generate_fake_data`
3) Run server:
   `python manage.py runserver`
