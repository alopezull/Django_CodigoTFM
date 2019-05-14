from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    url(r'^resultados/$', views.resultados, name='resultados'),
    url(r'^favicon.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico')),

]