from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Parcel,Point, Plot, Road, Irrigation
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

admin.site.unregister(Group)
admin.site.site_header = 'Land Pooling'
admin.site.site_title = 'Land Pooling Administration'
admin.site.index_title = 'Land Pooling Administration'

class ParcelAdmin1(LeafletGeoAdmin):
	#pass
	list_display =('owner_name','parcelno')

admin.site.register(Parcel, ParcelAdmin1)

class PointAdmin(LeafletGeoAdmin):
	#pass
	list_display =('pointid',)

admin.site.register(Point, PointAdmin)

class PlotAdmin(LeafletGeoAdmin):
	#pass
	list_display =('plot_no','plot_area')

admin.site.register(Plot, PlotAdmin)

class RoadAdmin(LeafletGeoAdmin):
	#pass
	list_display =('objectid',)

admin.site.register(Road, RoadAdmin)

class IrrigationAdmin(LeafletGeoAdmin):
	#pass
	list_display =('objectid',)

admin.site.register(Irrigation, IrrigationAdmin)