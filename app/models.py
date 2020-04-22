from django.db import models


class Steganographic(models.Model):
    """  Модель стеганографической группы """
    
    original_image = models.ImageField(upload_to='images/original/',
                                       verbose_name='Оригинальное изображение')
    
    watermark_image = models.ImageField(upload_to='images/watermark/', null=True, blank=True,
                                        verbose_name='Водяной знак')
    fractal_key_image = models.ImageField(upload_to='images/fractal/', null=True, blank=True,
                                          verbose_name='Фрактальный ключ')
    stego_image = models.ImageField(upload_to='images/stego/', null=True, blank=True,
                                    verbose_name='Стегоизображение')
    
    text = models.CharField(max_length=500, null=True, blank=True, default='Здесь могла бы быть умная цитата',
                            verbose_name='Данные для qr-кода')
    
    is_ok = models.BooleanField(default=False, verbose_name='Стегоконтейнер готов')
    has_errors = models.BooleanField(default=False, verbose_name='Есть ошибки')
    
    
    def __str__(self):
        return 'Стег. группа №{}, '.format(self.pk)
    
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
