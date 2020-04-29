from django.contrib import admin
from app.models import Steganographic, MainLog


class MainLogAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'client_address', 'message', 'raw', 'has_errors']


admin.site.register(Steganographic, )
admin.site.register(MainLog, MainLogAdmin)
