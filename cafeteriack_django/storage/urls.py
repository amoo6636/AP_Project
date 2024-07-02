from django.urls import path, include

from storage import views

urlpatterns = [
    path('storage/', views.StorageDetail.as_view()),
    path('update-storage/', views.updateStorage),
]


