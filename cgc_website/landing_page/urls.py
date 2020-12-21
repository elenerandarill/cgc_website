from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('en/home/', views.en_home, name='en_home'),
    # path('m/home/', views.m_home, name='m_home'),
]
