from django.urls import path
from apps.mascota.views import index, mascota_view, mascota_list
from apps.mascota.views import mascota_edit, mascota_delete, MascotaList

app_name = 'apps'
urlpatterns = [
    path('', index, name="index"),
    path('nuevo', mascota_view, name="mascota_crear"),
    path('lista', MascotaList.as_view(), name="mascota_listar"),
    path('editar/(?P<id_mascota>\d+)/', mascota_edit, name="mascota_editar"),
    path('eliminar/(?P<id_mascota>\d+)/',
         mascota_delete, name="mascota_eliminar"),
]
