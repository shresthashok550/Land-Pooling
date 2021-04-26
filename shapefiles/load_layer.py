import os
from django.contrib.gis.utils import LayerMapping
from .models import Plot1

plot1_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'plot_no': 'Plot_No',
    'ropani': 'ropani',
    'geom': 'MULTIPOLYGON',
}

final_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'../last/layout_final.shp'))

def run(verbose=True):
	lm = LayerMapping(Plot1, final_shp, plot1_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)