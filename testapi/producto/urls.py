from django.urls import path
from .views import get_producto,create_producto,producto_id,edit_producto,delete_producto

urlpatterns = [
    path ('todas/', get_producto),
    path('crear/', create_producto),
    path('por_id/<int:id>',producto_id),
    path('editar/<int:id>',edit_producto),
    path('eliminar/<int:id>',delete_producto)
]