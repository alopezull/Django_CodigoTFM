from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('upload.urls')),
    path('resultados/', include('upload.urls')),
    path('index/', include('upload.urls')),   
]
