from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Final, OldParcel, District, Parcel1, Plot, Plot1, Poi, Parcel,poi1, Joint
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

admin.site.unregister(Group)
admin.site.site_header = 'Land Pooling'

class FinalAdmin(LeafletGeoAdmin):
	#pass
	list_display =('plot_no','shape_area')

admin.site.register(Final, FinalAdmin)

class OldAdmin(LeafletGeoAdmin):
	#pass
	list_display =('owner_name','finalparce')

admin.site.register(OldParcel, OldAdmin)

class DistrictAdmin(LeafletGeoAdmin):
	#pass
	list_display =('district','province')

admin.site.register(District, DistrictAdmin)

class ParcelAdmin(LeafletGeoAdmin):
	#pass
	list_display =('owner_name','parcelno')

admin.site.register(Parcel1, ParcelAdmin)

class PlotAdmin(LeafletGeoAdmin):
	#pass
	list_display =('objectid','shape_area')

admin.site.register(Plot, PlotAdmin)

class PlotAdmin1(LeafletGeoAdmin):
	#pass
	list_display =('plot_no','shape_area')
	search_fields =('plot_no',)

admin.site.register(Plot1, PlotAdmin1)

class PoiAdmin1(LeafletGeoAdmin):
	#pass
	list_display =('point_id',)

admin.site.register(Poi, PoiAdmin1)

class ParcelAdmin1(LeafletGeoAdmin):
	#pass
	list_display =('owner_name','parcelno')

admin.site.register(Parcel, ParcelAdmin1)

class PoiAdmin(LeafletGeoAdmin):
	#pass
	list_display =('point_id',)

admin.site.register(poi1, PoiAdmin)

class JointAdmin(LeafletGeoAdmin):
	#pass
	list_display =('plot_no','plot_area')

admin.site.register(Joint, JointAdmin)