
from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_recepie, name='new_recepie'),
   
]

