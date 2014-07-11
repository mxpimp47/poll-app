from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_field = models.CharField(max_length=254)

    def __unicode__(self): 
    	return self.email_field