from django.urls import path, include

from storage import views

urlpatterns = [
    path('storage/', views.get_storage),
    path('update-storage/', views.updateStorage),
]


