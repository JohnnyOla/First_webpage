from django.db import models

# Create your models here.

class person(models.Model):
    name = models.CharField( max_length = 225, unique = True)
    mail = models.EmailField(max_length = 225, blank = True)
    def __unicode__(self):
        return self.name