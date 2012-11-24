from django.db import models

# Create your models here.
class Level(models.Model):
    guided_reading = models.CharField(max_length="1")
    grade_level = models.CharField(max_length="10")
    dra = models.CharField(max_length="10")

    def __unicode__(self):
        return str(self)

class Book(models.Model):

    title = models.CharField(max_length="255")
    level = models.ForeignKey(Level)
