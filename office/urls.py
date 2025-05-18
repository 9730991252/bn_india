from django.urls import path
from . import views

urlpatterns = [
    path('office_home/', views.office_home, name='office_home'),
    path('add_member/', views.add_member, name='add_member'),
    path('add_group/', views.add_group, name='add_group'),
    path('add_office_employee/', views.add_office_employee, name='add_office_employee'),
]