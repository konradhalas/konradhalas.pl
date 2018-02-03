from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    url = models.URLField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
