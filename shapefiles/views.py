from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Plot, Parcel, poi1, Joint
# Create your views here.

def plot_datasets(request):
	plots = serialize('geojson', Joint.objects.all())
	return HttpResponse(plots,content_type='json')

def parcel_datasets(request):
	parcels = serialize('geojson', Parcel.objects.all())
	return HttpResponse(parcels,content_type='json')

def poi_datasets(request):
	pois = serialize('geojson', poi1.objects.all())
	return HttpResponse(pois,content_type='json')