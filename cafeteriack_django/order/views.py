import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404 ,JsonResponse
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from product.models import Product, Vertical
from django.db.models import Sum, Min, Max
from datetime import timedelta, date, time, datetime

from .serializers import OrderSerializer, MyOrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            serializer.save(user=request.user, paid_amount=paid_amount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user = request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
    
def list_days_between(start_date, end_date):
    days_list = []
    current_date = start_date

    while current_date <= end_date:
        days_list.append(current_date)
        current_date += timedelta(days=1)

    return days_list

@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
class Chartview(APIView):
    def get(self, request, vertical_slug, format=None):

        if not request.user.is_staff:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        print(request.user)
        start_date = Order.objects.aggregate(min_date=Min('created_at'))['min_date'].date()
        end_date = Order.objects.aggregate(max_date=Max('created_at'))['max_date'].date()
        labels = list_days_between(start_date, end_date)
        mydata = []

        for label in labels:
            start_datetime = datetime.combine(label, time.min)
            end_datetime = datetime.combine(label, time.max)

            queryset = OrderItem.objects.filter(
                product__vertical__slug=vertical_slug,
                order__created_at__range=(start_datetime, end_datetime)
            ).annotate(total_quantity=Sum('quantity'))
            sales = 0
            for q in list(queryset.values('total_quantity')):
                sales += q['total_quantity']
            mydata.append(sales)

        return JsonResponse({'labels': labels, 'datasets': [{ 'label': 'sales', 'backgroundColor': '#f87979','data': mydata}]})