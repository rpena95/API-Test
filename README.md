This is a simple API project, it consist of 2 tables one for "categories" and another one for "products" both linked.

For this project we used
    *rest_framework_simplejwt',
    *rest_framework',

For authentication in endpoints we user
  *@permission_classes([IsAuthenticated])
and for rate limiting
  *@ratelimit(key= 'user_or_ip', rate='10/m')

Here is a description of URL's
    URL's for JWT Authentication 
      * api/token/
      * api/token/refresh/
    Base URL's for consulting both "Categories" & "Productos" 
      *categorias/
            *todas/ (Obtener todas las categorias)    
            *crear/ (Crear una nueva categoris)
            *por_id/<int:id> (Buscar categoria por ID)
            *editar/<int:id> (Editar categoria)
            *eliminar/<int:id> (Eliminar Categoria)
      *productos/
            *todas/ (Obtener todos los productos)    
            *crear/ (Crear un nuevo producto)
            *por_id/<int:id> (Buscar producto por ID)
            *editar/<int:id> (Editar producto)
            *eliminar/<int:id> (Eliminar producto)
