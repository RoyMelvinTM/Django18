from django.urls import path
from apps.mascota.views import index
app_name = 'apps'
urlpatterns = [
    path('', index),
]
