from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='images/photos/')
    published = models.BooleanField(default=True)
    created = models.DateTimeField('auto_add_now=True')

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[self.slug])
