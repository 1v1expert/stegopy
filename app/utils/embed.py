from app.utils.JuliaFractal import FractalImage
from app.utils.qrcode import Qrcode

from django.conf import settings

import qrcode


class Container(object):
    """ Главный стеганографический контейнер """
    def __init__(self, instance=None):
        assert instance is not None, 'Instance steganographic object is not be None'
        
        self.instance = instance
        self.fractal = None
        self.watermark = None
        
    def get_fractal_key(self):
        return FractalImage(default_palette=True, pk=self.instance.pk).generate()
    
    def get_qrcode(self):
        return Qrcode(self.instance.pk).generate(self.instance.text)
    
    def build(self):
        self.fractal = self.get_fractal_key()
        self.watermark = self.get_qrcode()
        
        self.instance.fractal_key_image = self.fractal.filename
        self.instance.watermark_image = self.watermark.filename
        
        self.instance.save()
