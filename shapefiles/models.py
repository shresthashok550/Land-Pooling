from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models

# class Final(models.Model):
#     shape_leng = models.FloatField()
#     shape_area = models.FloatField()
#     plot_no = models.BigIntegerField()
#     geom = gis_models.MultiPolygonField(srid=32644)

#     def __unicode__(self):
#     	return self.plot_no

#     class Meta:
#         verbose_name_plural = 'Final'

# class OldParcel(models.Model):
#     owner_name = models.CharField(max_length=50)
#     finalparce = models.BigIntegerField()
#     existing_a = models.FloatField()
#     ropani_aan = models.FloatField()
#     geom = gis_models.MultiPolygonField(srid=32644)

#     def __unicode__(self):
#     	return self.owner_name

#     class Meta:
#         verbose_name_plural = 'Old'

# class District(models.Model):
#     state_code = models.IntegerField()
#     district = models.CharField(max_length=50)
#     province = models.CharField(max_length=50)
#     geom = gis_models.MultiPolygonField(srid=4326)

#     def __unicode__(self):
#     	return self.district

#     class Meta:
#         verbose_name_plural = 'District'

# class Parcel1(models.Model):
#     owner_name = models.CharField(blank=True, null=True, max_length=50)
#     parcelno = models.FloatField(blank=True, null=True)
#     existing_a = models.FloatField(blank=True, null=True)
#     ropani_aan = models.FloatField(blank=True, null=True)
#     ropani = models.FloatField(blank=True, null=True)
#     aana = models.FloatField(blank=True, null=True)
#     paisa = models.FloatField(blank=True, null=True)
#     geom = gis_models.MultiPolygonField(blank=True, null=True, srid=4326)

#     def __unicode__(self):
#     	return self.owner_name

#     class Meta:
#         verbose_name_plural = 'Parcel1'

# class Plot(models.Model):
#     objectid = models.BigIntegerField()
#     shape_leng = models.FloatField()
#     shape_area = models.FloatField()
#     geom = gis_models.MultiPolygonField(srid=4326)

#     def __unicode__(self):
#     	return self.objectid

#     class Meta:
#         verbose_name_plural = 'Plot'

    
# class Plot1(models.Model):
#     shape_leng = models.FloatField()
#     shape_area = models.FloatField()
#     plot_no = models.BigIntegerField()
#     ropani = models.FloatField()
#     geom = gis_models.MultiPolygonField(srid=4326)

#     def __unicode__(self):
#     	return self.plot_no

#     class Meta:
#         verbose_name_plural = 'Plot1'

# class Poi(models.Model):
#     point_id = models.BigIntegerField()
#     geom = gis_models.MultiPointField(srid=4326)

#     def __unicode__(self):
#     	return self.point_id

#     class Meta:
#         verbose_name_plural = 'Poi'

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

class Joint(models.Model):
    plot_no = models.BigIntegerField()
    plot_perim = models.FloatField()
    plot_area = models.FloatField()
    ropani = models.FloatField()
    owner_name = models.CharField(max_length=50)
    existing_a = models.FloatField()
    owner_ropa = models.FloatField()
    owner_key = models.BigIntegerField()
    category = models.CharField(max_length=7)
    distri_are = models.FloatField()
    par_whole = models.CharField(max_length=1)
    distri_pa = models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)

    def __unicode__(self):
    	return self.plot_no

    class Meta:
        verbose_name_plural = 'Joint'

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