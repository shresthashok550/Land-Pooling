import os
from django.contrib.gis.utils import LayerMapping
from .models import Joint

joint_mapping = {
    'plot_no': 'PLOT_NO',
    'plot_perim': 'PLOT_PERIM',
    'plot_area': 'PLOT_AREA',
    'ropani': 'ROPANI',
    'owner_name': 'OWNER_NAME',
    'existing_a': 'EXISTING_A',
    'owner_ropa': 'OWNER_ROPA',
    'owner_key': 'OWNER_KEY',
    'category': 'CATEGORY',
    'distri_are': 'DISTRI_ARE',
    'par_whole': 'PAR_WHOLE',
    'distri_pa': 'DISTRI_PA',
    'geom': 'MULTIPOLYGON',
}

final_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'../shapefile/finaltable.shp'))

def run(verbose=True):
	lm = LayerMapping(Joint, final_shp, joint_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)