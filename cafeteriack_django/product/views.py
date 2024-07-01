from django.db.models import Q
from django.http import Http404 , HttpResponse

from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Product, Vertical
from .serializers import ProductSerializer, VerticalSerializer, AddProductSerializer

from django.contrib.admin.views.decorators import staff_member_required



class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, vertical_slug, product_slug):
        try:    
            return Product.objects.filter(vertical__slug=vertical_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, vertical_slug, product_slug, format=None):
        product = self.get_object(vertical_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    

    
class VerticalDetail(APIView):
    def get_object(self, vertical_slug):
        try:    
            return Vertical.objects.get(slug=vertical_slug)
        except Vertical.DoesNotExist:
            raise Http404
        
    def get(self, request, vertical_slug, format=None):
        vertical = self.get_object(vertical_slug)
        serializer = VerticalSerializer(vertical)
        return Response(serializer.data)
    
@api_view(['POST'])
def search(request):
    query = request.data.get('query','')

    if query:
        products = Product.objects.filter(Q(name__icontains=query)| Q(description__icontains=query))
        seriliazer = ProductSerializer(products, many=True)
        return Response(seriliazer.data)
    else:
        return Response({"products":[]})
    
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def addProduct(request):
    if request.user.is_staff:
        serializer = AddProductSerializer(data=request.data)
        if serializer.is_valid():
            try :
                serializer.save(thumbnail=None)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
