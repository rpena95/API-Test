from rest_framework.decorators import api_view, permission_classes
from django_ratelimit.decorators import ratelimit
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import CategoriaSerializer
from rest_framework import status
from .models import Categoria

@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['GET'])
def get_categorias(request):
    categoria = Categoria.objects.all()
    serializer = CategoriaSerializer(categoria, many=True)
    return Response(serializer.data)

@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['GET'])
def categoria_id(request, id):
    categoria = Categoria.objects.get(pk=id)
    serializer = CategoriaSerializer(categoria)
    return Response(serializer.data)

@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_categoria(request):
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response()

@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    serializer = CategoriaSerializer(categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@ratelimit(key= 'user_or_ip', rate='10/m')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    categoria.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

