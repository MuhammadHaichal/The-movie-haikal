from django.contrib import admin
from django.urls import path, include
    
urlpatterns = [
    path('', include('aplikasi_film.urls')),
    path("admin/", admin.site.urls),
]
