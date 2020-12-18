from django.db import models
from django.urls import reverse


class FreResults(models.Model):
    Temperature=models.FloatField(blank=True)

    Humidity =models.FloatField(blank=True)


    Moisture = models.FloatField(blank=True)

    Stype =models.FloatField(blank=True)
    Ctype = models.FloatField(blank=True)
    Nitrogen = models.FloatField(blank=True)
    Potassium = models.FloatField(blank=True)
    Phosphorous= models.FloatField(blank=True)

    classification = models.CharField(max_length =100)


    def get_absolute_url(self):
        return reverse("fertilizer",kwargs={"id":self.id})




    def __str__(self):
          return self.classification
