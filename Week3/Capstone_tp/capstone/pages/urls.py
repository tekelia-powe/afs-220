from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('mountain/', views.mountain, name='mountain'),
    path('mountain_tn/', views.mountain_tn, name='mountain_tn'),
    path('mountain_ca/', views.mountain_ca, name='mountain_ca'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('booked', views.booked, name='booked'),
    path('saved', views.saved, name='saved'),
]