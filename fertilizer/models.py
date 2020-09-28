from django.db import models


class FreResults(models.Model):
    Temperature=models.FloatField()

    Humidity =models.FloatField()


    Moisture = models.FloatField()

    Stype =models.FloatField()
    Ctype = models.FloatField()
    Nitrogen = models.FloatField()
    Potassium = models.FloatField()
    Phosphorous= models.FloatField()

    classification = models.CharField(max_length =100)




    def __str__(self):
          return self.classification
