from django.conf.urls import url

from app.views import index_view, encrypt_view, decrypt_view

app_name = 'app'

urlpatterns = [
    #url(r'^index', views.render_page),
    url(r'^$', index_view, name='index'),
    url(r'^(?P<result_id>[0-9]+)/$', encrypt_view, name='encrypt'),
    url(r'^(?P<result_id>[0-9]+)/decrypt/$', decrypt_view, name='decrypt')
    # url(r'^advanced/(?P<product_id>[0-9]+)-(?P<manufacturer_to>[0-9]+)/$',
    #     advanced_search_view, name='advanced_search'),
    # url(r'^from_file/$', search_from_file_view, name='search_from_file'),
]
