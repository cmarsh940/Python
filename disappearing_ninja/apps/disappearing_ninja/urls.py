from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ninja$', views.ninja, name='ninja'),
    url(r'ninja/(?P<color>\w+)$', views.ninja_color, name='ninja_color'),
]