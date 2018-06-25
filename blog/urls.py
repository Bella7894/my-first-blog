from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # http://127.0.0.1:8000/post/2/
    url(r'^post/(?P<id>[0-9]+)/$', views.post_detail, name='post_detail'),
]