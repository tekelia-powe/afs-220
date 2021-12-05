from django.urls import path

from . import views

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('security_questions', views.security_questions, name='security_questions'),
    path('ck_security_questions', views.ck_security_questions, name='ck_security_questions'),
    path('reset_password', views.reset_password, name='reset_password')
]