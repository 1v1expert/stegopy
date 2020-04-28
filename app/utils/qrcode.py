#!/usr/bin/python
import time

from django.conf import settings

import qrcode


class Qrcode(object):
    def __init__(self, pk=None):
        self.filename = 'images/watermark/watermark_{}.bmp'.format(pk if pk is not None else time.time())
    
    def generate(self, data):
        img = qrcode.make(data=data, box_size=5)
        
        img.save(settings.MEDIA_ROOT + '/' + self.filename)
        
        return self

