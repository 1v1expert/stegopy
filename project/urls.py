"""
Конфигурации корневаого роутинга

"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Стеганографическая система StegoPy"
admin.site.site_title = "Стеганографическая система StegoPy"
admin.site.index_title = "Стеганографическая система StegoPy"

urlpatterns = [
                  url(r'^', include('app.urls')),
                  url(r'^admin/', admin.site.urls),

              ] + static(settings.FILES_URL, document_root=settings.FILES_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)

print(urlpatterns)