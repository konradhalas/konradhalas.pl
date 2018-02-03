from django.db import models
from django.db.models import CASCADE

LANGUAGES = (
    ('polish', 'Polish'),
    ('english', 'English'),
)


class Talk(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slides = models.FileField()

    def __str__(self):
        return self.title


class Event(models.Model):
    talk = models.ForeignKey(Talk, related_name='events', on_delete=CASCADE)
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    date = models.DateField()
    language = models.CharField(choices=LANGUAGES, max_length=16)

    def __str__(self):
        return self.name
