import faker
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from bigfoot.models import User, Sighthing, Comment

NUSERS = 100
NSIGHTINGS = 200
NCOMMENTS = 4000


class Command(BaseCommand):
    help = "Generates fake data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [User, Sighthing, Comment]
        for m in models:
            m.objects.all().delete()

        faker_obj = faker.Faker()
        faker.Faker.seed(4321)  # always generate same data

        self.stdout.write("Generating users...")
        users = []
        for _ in range(NUSERS):
            user = User(
                username=faker_obj.unique.name(),
                email=faker_obj.unique.email()
            )
            user.save()

            users.append(user)

        self.stdout.write("Generating sightings...")
        sighthings = []
        for _ in range(NSIGHTINGS):
            sighthing = Sighthing(
                description=faker_obj.text(),
                title=faker_obj.text()[:80],
                owner=random.choice(users),
                date_added=faker_obj.date_between(start_date='-6m'),
            )
            sighthing.save()
            sighthings.append(sighthing)

        self.stdout.write("Generating comments...")
        for i in range(NCOMMENTS):
            if i % 5 == 0:
                # make every 5th comment done by a small set of users
                # Wow! They must *love* Bigfoot!
                owner = random.choice(users[:len(users) // 10])
            else:
                owner = random.choice(users)
            sighthing = random.choice(sighthings)

            comment = Comment(
                owner=owner,
                sighthing=sighthing,
                content=faker_obj.text(),
                date_added=faker_obj.date_between(
                    start_date=sighthing.date_added
                )
            )
            comment.save()
