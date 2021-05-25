from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Parcel,Point, Joint, Road, Irrigation
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

admin.site.unregister(Group)
admin.site.site_header = 'Land Pooling'
admin.site.site_title = 'Land Pooling Administration'
admin.site.index_title = 'Land Pooling Administration'

# class FinalAdmin(LeafletGeoAdmin):
# 	#pass
# 	list_display =('plot_no','shape_area')

# admin.site.register(Final, FinalAdmin)

# class OldAdmin(LeafletGeoAdmin):
# 	#pass
# 	list_display =('owner_name','finalparce')

# admin.site.register(OldParcel, OldAdmin)

# class DistrictAdmin(LeafletGeoAdmin):
# 	#pass
# 	list_display =('district','province')

# admin.site.register(District, DistrictAdmin)

# class ParcelAdmin(LeafletGeoAdmin):
# 	#pass
# 	list_display =('owner_name','parcelno')

# admin.site.register(Parcel1, ParcelAdmin)

# class PlotAdmin(LeafletGeoAdmin):
# 	#pass
# 	list_display =('objectid','shape_area')

# admin.site.register(Plot, PlotAdmin)

# class PlotAdmin1(LeafletGeoAdmin):
# 	#pass
# 	list_display =('plot_no','shape_area')
# 	search_fields =('plot_no',)

# admin.site.register(Plot1, PlotAdmin1)

# class PoiAdmin1(LeafletGeoAdmin):
# 	#pass
# 	list_display =('point_id',)

# admin.site.register(Poi, PoiAdmin1)

class ParcelAdmin1(LeafletGeoAdmin):
	#pass
	list_display =('owner_name','parcelno')

admin.site.register(Parcel, ParcelAdmin1)

class PointAdmin(LeafletGeoAdmin):
	#pass
	list_display =('pointid',)

admin.site.register(Point, PointAdmin)

class JointAdmin(LeafletGeoAdmin):
	#pass
	list_display =('plot_no','plot_area')

admin.site.register(Joint, JointAdmin)

class RoadAdmin(LeafletGeoAdmin):
	#pass
	list_display =('objectid',)

admin.site.register(Road, RoadAdmin)

class IrrigationAdmin(LeafletGeoAdmin):
	#pass
	list_display =('objectid',)

admin.site.register(Irrigation, IrrigationAdmin)