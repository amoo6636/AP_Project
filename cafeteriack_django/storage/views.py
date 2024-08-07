from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes


from .models import Storage


from .serializers import StorageSerializer



@api_view(['GET'])
def get_storage( request, format=None):
        storages = Storage.objects.all()
        serializer = StorageSerializer(storages, many=True)
        return Response(serializer.data)
    
        


@api_view(['POST'])
def updateStorage(request):
    sugar_amount = request.data.get('sugar_amount')
    coffee_amount = request.data.get('coffee_amount')
    flour_amount = request.data.get('flour_amount')
    chocolate_amount = request.data.get('chocolate_amount')
    sugar = Storage.objects.get(name="sugar")
    coffee = Storage.objects.get(name="coffee")
    flour = Storage.objects.get(name="flour")
    chocolate = Storage.objects.get(name="chocolate")
    if isinstance(sugar_amount, int) and isinstance(coffee_amount, int) and isinstance(flour_amount,int) and isinstance(chocolate_amount, int):
        sugar.amount = sugar_amount
        coffee.amount = coffee_amount
        flour.amount = flour_amount
        chocolate.amount= chocolate_amount
        sugar.save()
        coffee.save()
        flour.save()
        chocolate.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)




    

