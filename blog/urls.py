from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name="all-blogs-path"),
    path('<int:id>/', views.detail, name="detail")
]
