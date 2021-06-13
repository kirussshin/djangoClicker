from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/call_click/', views.call_click),
]
