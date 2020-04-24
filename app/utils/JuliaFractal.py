#!/usr/bin/python
import math, colorsys
import time
from PIL import Image, ImageDraw

from django.conf import settings


class FractalImage(object):
    def __init__(self, default_palette=False, pk=None):
        self.default_palette = default_palette
        
        self.l = 145
        self.dimensions = (self.l, self.l)
        self.scale = 1.0 / (self.dimensions[0] / 3)
        # center = (2.2, 1.5)       # Use this for Mandelbrot set
        c_x, c_y = 1.5, 1.5
        self.center = (c_x, c_y)  # Use this for Julia set
        self.iterate_max = 30
        self.colors_max = 2
    
        self.img = Image.new("RGB", self.dimensions)
        self.d = ImageDraw.Draw(self.img)
        
        name = 'fractal_{}.png'.format(pk if pk is not None else time.time())
        self.filename = 'images/fractal/' + name
    
    def generate(self):
        for y in range(self.dimensions[1]):  # Draw our image
            for x in range(self.dimensions[0]):
                c = complex(x * self.scale - self.center[0], y * self.scale - self.center[1])
            
                # n = iterate_mandelbrot(c)            # Use this for Mandelbrot set
                # n = iterate_mandelbrot(complex(0.3, 0.6), c)  # Use this for Julia set
                n = self.my_mandelbrot(c)
            
                if n is None:
                    v = 1
                else:
                    v = n / 100.0
            
                self.d.point(
                    (x, y), fill=self.get_palette()[int(v * (self.colors_max - 1))]
                )

        del self.d

        self.img.save(settings.MEDIA_ROOT + '/' + self.filename)
        
        return self
    
    def iterate_mandelbrot(self, c, z=0):
        """ Calculate the mandelbrot sequence for the point c with start value z """
        for n in range(self.iterate_max + 1):
            z = z * z + c
            if abs(z) > 2:
                return n
        return None
    
    def my_mandelbrot(self, z, c=complex(-0.76643, 0.16471)):
        """ Calculate the mandelbrot sequence for the point c with start value z """
        for n in range(self.iterate_max + 1):
            z = z * z + c
            if abs(z) > self.calculateR(c):
                return n
        return None
    
    @staticmethod
    def calculateR(c):
        return (1 + math.sqrt(1 + 4 * abs(c))) / 2
    
    def get_palette(self):
        """ Calculate a tolerable palette """
        
        if self.default_palette:
            return [(0, 0, 0), (255, 255, 255)]
        
        palette = [0] * self.colors_max
        for i in range(self.colors_max):
            f = 1 - abs((float(i) / self.colors_max - 1) ** 15)
            r, g, b = colorsys.hsv_to_rgb(.66 + f / 3, 1 - f / 2, f)
            palette[i] = (int(r * 255), int(g * 255), int(b * 255))
        
        return palette
