from app.utils.JuliaFractal import FractalImage
from app.utils.qrcode import Qrcode
from app.stego_lsb import LSBSteg

from django.conf import settings


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
    
    def hide_lsb(self):
        output_filename = 'images/fractal_with_watermark/fractal_with_watermark_{}.png'.format(self.instance.pk)
        LSBSteg.hide_data(self.fractal.filename,
                          self.watermark.filename,
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
        
        self.hide_lsb()
        
        self.instance.save()
