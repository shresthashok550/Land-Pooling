import os
from django.contrib.gis.utils import LayerMapping
from .models import OldParcel

parcel_mapping = {
    'owner_name': 'Owner_Name',
    'finalparce': 'finalparce',
    'existing_a': 'Existing_A',
    'ropani_aan': 'Ropani_Aan',
    'geom': 'MULTIPOLYGON',
}

final_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'../final/existing_parcel1111.shp'))

def run(verbose=True):
	lm = LayerMapping(OldParcel, final_shp, parcel_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)