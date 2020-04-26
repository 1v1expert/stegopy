import cv2
import numpy
import numpy as np
import scipy.interpolate
import scipy.misc


class DammstenderDeleigle(object):
    """ Метод Дармстедтера-Делейгла-Квисквотера-Макка """
    
    def __init__(self, input_image_path, input_file_path=None, steg_image_path=None):
        img = cv2.imread(input_image_path)
        # im_color = cv2.applyColorMap(img, cv2.COLORMAP_HSV)
        
        self.R = img[:, :, 0] # красный канал
        self.G = img[:, :, 1] # зеленый канал
        self.B = img[:, :, 2] # синий канал - модифицируемый
        # print(self.B)
        
        self.X = len(self.B)   # размер по X
        self.Y = len(self.B[1])   # размер по Y
        self.N = 8 # размер блока
        
        self.Ns = int(self.X * self.Y / (self.N * self.N)) # количество блоков
        
        self.fractal_key_with_watermark = cv2.imread(input_file_path) # встраиваемое изображение
        self.fractal_key_with_watermarkR = self.fractal_key_with_watermark[:, :, 0] # красный канал встр. изобр.
        
        # print(self.fractal_key_with_watermarkR)
        self.S = self.segment()
        
        BW = self.getBW()
        Mvec_bin = self.getBWbits(BW)
        
        self.Lm = len(Mvec_bin)
        
        self.Zone()
        # print(Lm)
        
        # print(self.R, '\n----\n', self.B, '\n----\n' , self.G)#, self.B)
    
    def segment(self):
        """ Разбиение контейнера на сигменты """
        
        c1 = 1  # левая граница столбцов
        c2 = self.N # правая граница столбцов
        
        S = [] # массив(вектор) формируем из матрицы X * Y блоками N * N
        
        for b in range(self.Ns):
            r1 = (self.N * (b-1) + 1) % self.X
            r2 = r1 + self.N -1
            S.append(self.B[r1:r2, c1:c2]) # записываем блок в вектор
            if r2 == self.X:
                c1 = c1 + self.N
                c2 = c2 + self.N
        return S
        # print(S[18220])
        
    def getBW(self):
        
        BW = []
        for i in range(len(self.fractal_key_with_watermarkR)): # переводим матрицу в вектор
            for j in range(len(self.fractal_key_with_watermarkR[0])):
                pixel = self.fractal_key_with_watermarkR[i, j]
                
                if pixel > 127:  # делаем изображение чёрно-белым
                    BW.append(255)
                else:
                    BW.append(0)

        return BW
    
    def getBWbits(self, BW):
        """ получаем биты встраиваемого изображения """
        bytes = numpy.fromiter(BW, dtype="uint8")
        return numpy.unpackbits(bytes)
    
    def Zone(self):
        """ разбиение на зоны """
        print(self.Lm, len(self.S))
        for s in range(self.Lm):
            f = numpy.zeros(self.N * self.N)
            Block = self.S[s]
            
            p = 0
            for i in range(len(Block)):
                for j in range(len(Block[0])):
                    f[p] = Block[i, j]
                    p += 1
                    
            # print(f)
            F = sorted(f)
            # print(F)
            r = 10
            Ksi = numpy.zeros(r)
            Phi = numpy.zeros(r)

            
            
            for x in range(1, r):
                Ksi[x] = x * round(self.N * self.N / (r - 1))
                
            Ksi[0] = 1
            Ksi[r-1] = self.N * self.N
            
            for x in range(len(Ksi)):
                # print(Ksi[x])
                # print(x, F[Ksi[x]-1])
                Phi[x] = F[int(Ksi[x])-1]
            
            Smax = 0
            alpha = 0
            
            # print(Ksi)
            Spline = scipy.interpolate.PchipInterpolator(Ksi, Phi)
            deriv = Spline.derivative()
            for w in range(self.N * self.N):
                sp = deriv(w)
                if sp > Smax:
                    Smax = sp
                    alpha = w
            if alpha == 0:
                alpha = self.N * self.N /2
            elif alpha == 1:
                alpha = 2
            elif alpha == self.N * self.N:
                alpha = self.N * self.N - 1
                
            T1 = 6
            T2 = 3
            B_min = 0
            B_pl = 0
            Zone1 = numpy.zeros((self.N, self.N))
            
            if Smax < T1:
                for i in range(self.N):
                    for j in range(self.N):
                        Zone1[i, j] = (j + 1) % 2 + 1
                        
            if Smax > T1:
                pass
                    # print(deriv(w))
            # deriv = scipy.misc.derivative(Spline)

if __name__ == '__main__':
    DammstenderDeleigle('gg.jpg', input_file_path='key.png')