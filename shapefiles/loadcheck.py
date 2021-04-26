import os
from django.contrib.gis.utils import LayerMapping
from .models import Parcel

parcel_mapping = {
    'owner_name': 'OWNER_NAME',
    'parcelno': 'PARCELNO',
    'existing_a': 'EXISTING_A',
    'ropani_aan': 'ROPANI_AAN',
    'category': 'CATEGORY',
    'ropani': 'ROPANI',
    'aana': 'AANA',
    'paisa': 'PAISA',
    'geom': 'MULTIPOLYGON',
}

final_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'../shapefile/final_existing_parcel.shp'))

def run(verbose=True):
	lm = LayerMapping(Parcel, final_shp, parcel_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)