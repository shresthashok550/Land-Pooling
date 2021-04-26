from django.urls import path

from .views import plot_datasets, parcel_datasets, poi_datasets

urlpatterns = [
	path('plot', plot_datasets, name='plot'),
	path('parcel', parcel_datasets, name='parcel'),
	path('poi', poi_datasets, name='poi'),
]