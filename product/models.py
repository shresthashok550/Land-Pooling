from django.db import models
from django.contrib.gis.db import models as gis_model
from datetime import datetime

# Create your models here.
class Product(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    product_header = models.CharField(max_length=50)
    product_body = models.CharField(max_length=5000)
    plot_no = models.BigIntegerField(null=True)
    product_date = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField()
    lng = models.FloatField()
    

    def __str__(self):
        return self.first_name
