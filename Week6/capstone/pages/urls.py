from django.urls import path
from django.contrib.auth import views

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
    path('beach/', views.beach, name='beach'),
    path('beach_tx/', views.beach_tx, name='beach_tx'),
    path('beach_fl/', views.beach_fl, name='beach_fl'),
    path('beach_ca/', views.beach_ca, name='beach_ca'),
    path('jungle/', views.jungle, name='jungle'),
    path('jungle_be/', views.jungle_be, name='jungle_be'),
    path('jungle_br/', views.jungle_br, name='jungle_br'),
    path('jungle_cr/', views.jungle_cr, name='jungle_cr'),
    path('delete_booking/<id>', views.delete_booking, name='delete_booking'),
    path('unsave_booking/<id>', views.unsave_booking, name='unsave_booking'),
    path('dashboard', views.dashboard, name='dashboard')
]