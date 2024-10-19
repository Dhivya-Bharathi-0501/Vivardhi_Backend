from django.urls import path
from . import views

urlpatterns = [
    path('get-resources/', views.get_resources, name='get_resources'),
]