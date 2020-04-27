from app.utils.JuliaFractal import FractalImage
from app.utils.qrcode import Qrcode
from app.stego_lsb import LSBSteg

from django.conf import settings

# from datetime import datetime
from time import gmtime, strftime
import time


class Container(object):
    """ Главный стеганографический контейнер """
    def __init__(self, instance=None):
        assert instance is not None, 'Instance steganographic object is not be None'
        
        self.start_time = time.time()
        
        self.instance = instance
        self.fractal = None
        self.watermark = None
        self.original_image = self.instance.original_image
        # self.fractal_key_with_watermark = None
        
    def get_fractal_key(self):
        return FractalImage(default_palette=True, pk=self.instance.pk).generate()
    
    def get_qrcode(self):
        return Qrcode(self.instance.pk).generate(self.instance.text)
    
    def hide_lsb(self):
        output_filename = 'images/fractal_with_watermark/fractal_with_watermark_{}.png'.format(self.instance.pk)
        LSBSteg.hide_data(settings.MEDIA_ROOT + '/' + self.fractal.filename,
                          settings.MEDIA_ROOT + '/' + self.watermark.filename,
                          settings.MEDIA_ROOT + '/' + output_filename,
                          1,
                          1
                          )
        return output_filename
    
    def dammstender_deleigle(self):
        output_filename = 'images/stego/stego_{}.png'.format(self.instance.pk)
        LSBSteg.hide_data(settings.MEDIA_ROOT + '/' + self.original_image.name,
                          settings.MEDIA_ROOT + '/' + self.instance.fractal_key_with_watermark.name,
                          settings.MEDIA_ROOT + '/' + output_filename,
                          1,
                          1
                          )
        return output_filename
    
    def build(self):
        self.fractal = self.get_fractal_key()
        self.watermark = self.get_qrcode()
        
        self.instance.fractal_key_image = self.fractal.filename
        self.instance.watermark_image = self.watermark.filename
        
        self.instance.fractal_key_with_watermark = self.hide_lsb()
        
        self.instance.stego_image = self.dammstender_deleigle()
        
        self.instance.save()

        print(strftime("%H:%M:%S", gmtime(time.time() - self.start_time)))