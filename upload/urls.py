from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    url(r'^resultados/$', views.resultados, name='resultados'),



]