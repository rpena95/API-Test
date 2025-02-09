from rest_framework.decorators import api_view, permission_classes
from django_ratelimit.decorators import ratelimit
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import ProductoSerializer
from rest_framework import status
from .models import Producto

@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['GET'])
def get_producto(request):
    producto = Producto.objects.all()
    serializer = ProductoSerializer(producto, many=True)
    return Response(serializer.data)


@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['GET'])
def producto_id(request, id):
    producto = Producto.objects.get(pk=id)
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)

@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_producto(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response()

@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_producto(request, id):
    producto = Producto.objects.get(pk=id)
    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_producto(request, id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
