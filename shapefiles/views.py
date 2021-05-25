from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Parcel, Point, Joint, Road, Irrigation
# Create your views here.

def plot_datasets(request):
	plots = serialize('geojson', Joint.objects.all())
	return HttpResponse(plots,content_type='json')

def parcel_datasets(request):
	parcels = serialize('geojson', Parcel.objects.all())
	return HttpResponse(parcels,content_type='json')

def poi_datasets(request):
	pois = serialize('geojson', Point.objects.all())
	return HttpResponse(pois,content_type='json')

def road_datasets(request):
	road = serialize('geojson', Road.objects.all())
	return HttpResponse(road,content_type='json')

def irrigation_datasets(request):
	irrigation = serialize('geojson', Irrigation.objects.all())
	return HttpResponse(irrigation,content_type='json')