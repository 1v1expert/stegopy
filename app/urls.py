from django.conf.urls import url

from app.views import index_view

app_name = 'app'

urlpatterns = [
    #url(r'^index', views.render_page),
    url(r'^$', index_view, name='index'),
    # url(r'^advanced/(?P<product_id>[0-9]+)-(?P<manufacturer_to>[0-9]+)/$',
    #     advanced_search_view, name='advanced_search'),
    # url(r'^from_file/$', search_from_file_view, name='search_from_file'),
]
