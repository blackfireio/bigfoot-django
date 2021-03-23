import datetime

from django.db import models


class User(models.Model):
    email = models.CharField(max_length=180, unique=True)
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        return f'https://avatars.dicebear.com/4.5/api/human/{self.email}.svg?mood[]=happy'

    def get_recent_comments_count(self):
        return Comment.objects.filter(
            owner__id=self.id,
            date_added__gt=datetime.datetime.now() - datetime.timedelta(days=3 * 30)
        ).count()


class Sighting(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField()
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.content
