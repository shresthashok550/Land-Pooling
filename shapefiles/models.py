from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models

class Parcel(models.Model):
    owner_name = models.CharField(max_length=50)
    parcelno = models.BigIntegerField()
    existing_a = models.FloatField()
    ropani_aan = models.FloatField()
    category = models.CharField(max_length=7)
    ropani = models.BigIntegerField()
    aana = models.BigIntegerField()
    paisa = models.BigIntegerField()
    geom = gis_models.MultiPolygonField(srid=4326)

    def __unicode__(self):
    	return self.owner_name

    class Meta:
        verbose_name_plural = 'Parcel'

class Point(models.Model):
    pointid = models.IntegerField()
    geom = gis_models.MultiPointField(srid=4326)

    def __unicode__(self):
    	return self.point_id

    class Meta:
        verbose_name_plural = 'Point'

class Plot(models.Model):
    plot_no = models.IntegerField(primary_key=True)
    plot_perim = models.FloatField()
    plot_area = models.FloatField()
    ropani = models.FloatField()
    category = models.CharField(max_length=7)
    owner_name = models.CharField(max_length=50)
    owner1 = models.CharField(max_length=50)
    owner2 = models.CharField(max_length=30)
    owner3 = models.CharField(max_length=30)
    owner4 = models.CharField(max_length=30)
    owner5 = models.CharField(max_length=30)
    existing_a = models.FloatField()
    existing1 = models.FloatField()
    existing2 = models.FloatField()
    existing3 = models.FloatField()
    existing4 = models.FloatField()
    existing5 = models.FloatField()
    owner_ropa = models.FloatField()
    owner_r1 = models.FloatField()
    owner_r2 = models.FloatField()
    owner_r3 = models.FloatField()
    owner_r4 = models.FloatField()
    owner_r5 = models.FloatField()
    owner_key = models.FloatField()
    owner_key1 = models.BigIntegerField()
    owner_key2 = models.BigIntegerField()
    owner_key3 = models.BigIntegerField()
    owner_key4 = models.BigIntegerField()
    owner_key5 = models.BigIntegerField()
    distri_are = models.FloatField()
    distri_ar1 = models.FloatField()
    distri_ar2 = models.FloatField()
    distri_ar3 = models.FloatField()
    distri_ar4 = models.FloatField()
    distri_ar5 = models.FloatField()
    par_whole = models.CharField(max_length=1)
    par_whole1 = models.CharField(max_length=10)
    par_whole2 = models.CharField(max_length=10)
    par_whole3 = models.CharField(max_length=10)
    par_whole4 = models.CharField(max_length=10)
    par_whole5 = models.CharField(max_length=10)
    distri_pa = models.FloatField()
    distri_pa1 = models.FloatField()
    distri_pa2 = models.FloatField()
    distri_pa3 = models.FloatField()
    distri_pa4 = models.FloatField()
    distri_pa5 = models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)

    def __unicode__(self):
    	return self.plot_no

    class Meta:
        verbose_name_plural = 'Plot'

class Road(models.Model):
    objectid = models.BigIntegerField()
    shape_leng = models.FloatField()
    geom = gis_models.MultiLineStringField(srid=4326)

    def __unicode__(self):
    	return self.objectid

    class Meta:
        verbose_name_plural = 'Road'

class Irrigation(models.Model):
    objectid = models.BigIntegerField()
    shape_leng = models.FloatField()
    geom = gis_models.MultiLineStringField(srid=4326)

    def __unicode__(self):
    	return self.objectid

    class Meta:
        verbose_name_plural = 'Irrigation'