# Generated by Django 3.0.5 on 2020-04-28 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_steganographic_fractal_key_with_watermark'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='action time')),
                ('client_address', models.TextField(blank=True, max_length=100, null=True, verbose_name='Адрес клиента')),
                ('message', models.TextField(blank=True, verbose_name='message')),
                ('raw', models.TextField(blank=True, null=True, verbose_name='Голые данные')),
                ('has_errors', models.BooleanField(default=False, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Лог активности',
                'verbose_name_plural': 'Логи активности',
                'ordering': ('-action_time',),
            },
        ),
    ]
