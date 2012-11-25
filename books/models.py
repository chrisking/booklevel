from django.db import models

# Create your models here.
class Level(models.Model):
    guided_reading = models.CharField(max_length="1")
    grade_level = models.CharField(max_length="10")
    dra = models.CharField(max_length="10")

    def __unicode__(self):
        return str(self.guided_reading)

class Book(models.Model):

    title = models.CharField(max_length="255")
    level = models.ForeignKey(Level)
    grade_level = models.CharField(max_length="10", null=True, blank=True)
    dra = models.CharField(max_length="10", null=True, blank=True)

    #Inventory Fields
    #number_of_copies = models.IntegerField(default=1)
    #number_available = models.IntegerField(default=1)
    def save(self, *args, **kwargs):
        """
        override exists to assign the other parameters
        """
        self.grade_level = self.set_grade_level()
        self.dra = self.set_DRA()
        super(Book, self).save(*args, **kwargs) # Call the "real" save() method.

    def set_grade_level(self):
        return str(self.level.grade_level)

    def set_DRA(self):
        return str(self.level.dra)