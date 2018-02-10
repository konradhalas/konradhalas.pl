from django.db import models
from django.db.models import CASCADE

from utils.models import SlugifyUploadTo

LANGUAGES = (
    ('polish', 'Polish'),
    ('english', 'English'),
)


class Talk(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    slides = models.FileField(upload_to=SlugifyUploadTo(path='slides', fields=['title']), null=True, blank=True)

    def start_year(self):
        event = self.events.last()
        return event.date.year if event else None

    def end_year(self):
        event = self.events.first()
        return event.date.year if event else None

    def __str__(self):
        return self.title


class Event(models.Model):
    talk = models.ForeignKey(Talk, related_name='events', on_delete=CASCADE)
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    date = models.DateField()
    language = models.CharField(choices=LANGUAGES, max_length=16)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
