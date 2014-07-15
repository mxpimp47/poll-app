from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField('auto_add_now=True')

    class Meta:
        ordering = ['-created']
        

    def __unicode__(self):
    	return self.title


    def get_absolute_url(self):
        return reverse('blog-detail', args=[self.slug])
