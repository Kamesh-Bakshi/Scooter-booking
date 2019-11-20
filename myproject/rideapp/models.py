from django.db import models

# Create your models here.
class scooters(models.Model):
    uniqueid = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()

    def __int__(self):
        return self.uniqueid

    def location(self):
        return [self.lat,self.long]
