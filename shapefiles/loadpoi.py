import os
from django.contrib.gis.utils import LayerMapping
from .models import poi1

poi_mapping = {
    'point_id': 'Point_id',
    'geom': 'MULTIPOINT',
}

final_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'../shapefile/poi.shp'))

def run(verbose=True):
	lm = LayerMapping(poi1, final_shp, poi_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)