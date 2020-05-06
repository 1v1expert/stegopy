from django.db import models
from app.utils.embed import Container
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Steganographic(models.Model):
    """  Модель стеганографической группы """
    
    original_image = models.ImageField(upload_to='images/original/', null=True, blank=True,
                                       verbose_name='Оригинальное изображение')
    
    watermark_image = models.ImageField(upload_to='images/watermark/', null=True, blank=True,
                                        verbose_name='Водяной знак')
    fractal_key_image = models.ImageField(upload_to='images/fractal/', null=True, blank=True,
                                          verbose_name='Фрактальный ключ')
    stego_image = models.ImageField(upload_to='images/stego/', null=True, blank=True,
                                    verbose_name='Стегоизображение')
    
    text = models.CharField(max_length=500, null=True, blank=True, default='Здесь могла бы быть умная цитата',
                            verbose_name='Данные для qr-кода')

    fractal_key_with_watermark = models.ImageField(upload_to='images/fractal_with_watermark/', null=True, blank=True,
                                                   verbose_name='Ключ со встроенным ЦВЗ')
    
    is_decrypt = models.BooleanField(default=True, verbose_name='Сокрытие')
    is_ok = models.BooleanField(default=False, verbose_name='Успешно')
    has_errors = models.BooleanField(default=False, verbose_name='Есть ошибки')
    
    tech_info = models.TextField(null=True, blank=True, verbose_name='Тех. информация о контейнере')
    
    def __str__(self):
        return 'Стег. группа №{}, '.format(self.pk)
    
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
    
    def create_stegocontainer(self):
        Container(instance=self).build()


class MainLog(models.Model):
    action_time = models.DateTimeField(_('action time'), default=timezone.now, editable=False, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, blank=True, null=True, verbose_name=_('user'), )
    client_address = models.TextField(max_length=100, blank=True, null=True, verbose_name="Адрес клиента")
    message = models.TextField(_('message'), blank=True)
    raw = models.TextField(null=True, blank=True, verbose_name="Голые данные")
    has_errors = models.BooleanField(default=False, null=True)
    
    class Meta:
        verbose_name = "Лог активности"
        verbose_name_plural = "Логи активности"
        ordering = ('-action_time',)
    
    def __str__(self):
        return '{}; {}'.format(self.user, self.message)