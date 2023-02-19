
from django.contrib import admin
from django.urls import path,include
from myapp import views
from  QuerySet import views_1


urlpatterns = [
    path('', views.index),
    path('p1/', views.first_page),
    path('p2/', views.second_page),
    path('test/', views_1.testing),



]
