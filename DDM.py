import cv2
import numpy

class DammstenderDeleigle(object):
    """ Метод Дармстедтера-Делейгла-Квисквотера-Макка """
    
    def __init__(self, input_image_path, input_file_path=None, steg_image_path=None):
        img = cv2.imread(input_image_path)
        # im_color = cv2.applyColorMap(img, cv2.COLORMAP_HSV)
        
        self.R = img[:, :, 0] # красный канал
        self.G = img[:, :, 1] # зеленый канал
        self.B = img[:, :, 2] # синий канал - модифицируемый
        
        self.X = len(self.B)   # размер по X
        self.Y = len(self.B[1])   # размер по Y
        self.N = 8 # размер блока
        
        self.Ns = int(self.X * self.Y / (self.N * self.N)) # количество блоков
        
        self.fractal_key_with_watermark = cv2.imread(input_file_path) # встраиваемое изображение
        self.fractal_key_with_watermarkR = self.fractal_key_with_watermark[:, :, 0] # красный канал встр. изобр.
        
        # print(self.fractal_key_with_watermarkR)
        self.segment()
        
        BW = self.getBW()
        Mvec_bin = self.getBWbits(BW)
        
        Lm = len(Mvec_bin)
        
        # print(Lm)
        
        # print(self.R, '\n----\n', self.B, '\n----\n' , self.G)#, self.B)
    
    def segment(self):
        """ Разбиение контейнера на сигменты """
        
        c1 = 1  # левая граница столбцов
        c2 = self.N # правая граница столбцов
        
        S = [] # массив(вектор) формируем из матрицы X * Y блоками N * N
        
        for b in range(1, self.Ns):
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
    

if __name__ == '__main__':
    DammstenderDeleigle('SuMoNeDone.bmp', input_file_path='key.png')