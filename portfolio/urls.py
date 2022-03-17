from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-path"),
    path('works/', views.works, name="works-path"),
    path('social/', views.contact, name="contact-path"),
]
