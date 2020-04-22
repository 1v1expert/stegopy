from django.contrib import admin
from app.models import Steganographic


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'email', 'is_subscriber', 'text']


# admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(Steganographic, )