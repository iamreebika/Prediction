from django.db import models
from django.urls import reverse


class CropResults(models.Model):
    Temperature=models.FloatField()

    Humidity =models.FloatField()


    Moisture = models.FloatField()

    Soiltype =models.FloatField()
    pH = models.FloatField()


    classification = models.CharField(max_length =100)

    def get_absolute_url(self):
        return reverse("Crop1:Crop1-index",kwargs={"id":self.id})

