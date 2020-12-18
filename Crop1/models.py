from django.db import models

class CropResult(models.Model):
    Temperature=models.FloatField(blank=True)

    Humidity =models.FloatField(blank=True)


    Moisture = models.FloatField(blank=True)

    Stype =models.FloatField(blank=True)
    Ctype = models.FloatField(blank=True)
    Ph = models.FloatField(blank=True)

    classification = models.CharField(max_length =100)
