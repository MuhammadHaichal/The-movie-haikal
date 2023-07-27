from django.urls import path, re_path
from .views import index, detailsMovie

urlpatterns = [
        path('', index, name='indexMovie'),
        re_path('details/(?P<pk>[0-9]+)/', detailsMovie, name='detailMovie'),
        ]
