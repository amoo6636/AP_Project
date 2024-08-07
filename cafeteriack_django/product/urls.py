from django.urls import path, include

from product import views


urlpatterns = [
    path('popular-products/', views.PopularProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:vertical_slug>/<slug:product_slug>/',views.ProductDetail.as_view()),
    path('products/<slug:vertical_slug>/',views.VerticalDetail.as_view()),
    path('add/',views.addProduct),
    path('isstaff/',views.UserDetailView.as_view()),

]