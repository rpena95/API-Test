from django.urls import path
from .views import get_categorias, create_categoria, categoria_id, edit_categoria, delete_categoria

urlpatterns = [
    path ('todas/', get_categorias),
    path('crear/', create_categoria),
    path('por_id/<int:id>',categoria_id),
    path('editar/<int:id>',edit_categoria),
    path('eliminar/<int:id>',delete_categoria)
]