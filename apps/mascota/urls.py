from django.urls import path
from apps.mascota.views import index, mascota_view
from apps.mascota.views import mascota_edit
from apps.mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

app_name = 'apps'
urlpatterns = [
    path('', index, name="index"),
    path('nuevo', MascotaCreate.as_view(), name="mascota_crear"),
    path('lista', MascotaList.as_view(), name="mascota_listar"),
    path('editar/(?P<pk>\d+)/',
         MascotaUpdate.as_view(), name="mascota_editar"),
    path('eliminar/(?P<pk>\d+)/',
         MascotaDelete.as_view(), name="mascota_eliminar"),
]
