import os
from django.contrib.gis.utils import LayerMapping
from .models import District

district_mapping = {
    'state_code': 'STATE_CODE',
    'district': 'DISTRICT',
    'province': 'Province',
    'geom': 'MULTIPOLYGON',
}

final_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'../final/Districts.shp'))

def run(verbose=True):
	lm = LayerMapping(District, final_shp, district_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)