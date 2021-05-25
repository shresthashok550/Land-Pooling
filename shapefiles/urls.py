from django.urls import path

from .views import plot_datasets, parcel_datasets, poi_datasets, road_datasets, irrigation_datasets

urlpatterns = [
	path('plot', plot_datasets, name='plot'),
	path('parcel', parcel_datasets, name='parcel'),
	path('road', road_datasets, name='road'),
	path('poi', poi_datasets, name='poi'),
	path('irrigation', irrigation_datasets, name='irrigation'),
]