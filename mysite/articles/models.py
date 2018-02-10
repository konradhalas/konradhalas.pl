import markdown
from django.db import models
from django.urls import reverse
from markdown_newtab import NewTabExtension

from utils.models import SlugifyUploadTo


class Article(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to=SlugifyUploadTo(path='articles', fields=['title']))
    content = models.TextField()
    publish_date = models.DateField()
    update_date = models.DateField()
    is_public = models.BooleanField()

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_details', kwargs={'slug': self.slug})

    @property
    def html_content(self):
        return markdown.markdown(self.content, extensions=[
            'markdown.extensions.codehilite',
            NewTabExtension(),
        ])
