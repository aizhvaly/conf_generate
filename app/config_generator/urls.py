from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_main),
    path('pyapp/', views.config_generator),
]  #name=""




