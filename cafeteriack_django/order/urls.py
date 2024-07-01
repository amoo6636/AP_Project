from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),
    path('charts/<slug:vertical_slug>/',views.Chartview.as_view()),
]