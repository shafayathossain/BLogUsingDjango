from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^create$', views.post_create),
    url(r'^(?P<id>\d+)/$', views.post_detail, name="detail"),
    url(r'^$', views.post_list),
    url(r'^(?P<id>\d+)/edit$', views.post_update),
    url(r'^delete$', views.post_delete),

]