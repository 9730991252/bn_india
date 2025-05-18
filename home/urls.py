from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('office_login/', views.office_login, name='office_login'),
]