from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    url(r'^resultados/$', views.resultados, name='resultados'),
    url(r'^prueba1/$', views.prueba1, name='prueba1'),
]