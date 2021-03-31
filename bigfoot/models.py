import datetime

from django.db import models


class User(models.Model):
    email = models.CharField(max_length=180, unique=True)
    username = models.CharField(max_length=100, unique=True)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

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


class Sighting(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField()
    score = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super(Sighting, self).__init__(*args, **kwargs)


class Comment(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)
    date_added = models.DateTimeField()

    def __init__(self, *args, **kwargs):
        super(Comment, self).__init__(*args, **kwargs)
