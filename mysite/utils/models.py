import os

from django.utils.deconstruct import deconstructible
from django.utils.text import slugify

@deconstructible
class SlugifyUploadTo(object):

    def __init__(self, path, fields):
        self.path = path
        self.fields = fields

    def __call__(self, instance, filename):
        extension = filename.split('.')[-1]
        slug = slugify(' '.join([str(getattr(instance, field)) for field in self.fields]))
        new_filename = '{0}.{1}'.format(slug, extension)
        return os.path.join(self.path, new_filename)
