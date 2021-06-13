from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('api/call_click/', views.call_click),
    path('api/buy_boost/', views.buy_boost),
]
