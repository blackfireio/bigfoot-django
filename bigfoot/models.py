import datetime

from django.db import models


class User(models.Model):
    email = models.CharField(max_length=180, unique=True)
    username = models.CharField(max_length=100, unique=True)

    def get_avatar_url(self):
        return 'https://avatars.dicebear.com/4.5/api/human/%s.svg?mood[]=happy' % (
            self.email
        )

    def get_recent_comments_count(self):
        recent_comment_count = 0
        comments = Comment.objects.filter(owner__id=self.id)
        for comment in comments.all():
            if comment.date_added.month - datetime.datetime.now().month <= 3:
                recent_comment_count += 1

        return recent_comment_count


class Sighthing(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField()
    score = models.IntegerField(default=0)


class Comment(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sighthing = models.ForeignKey(Sighthing, on_delete=models.CASCADE)
    date_added = models.DateTimeField()
