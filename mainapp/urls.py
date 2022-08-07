from django.urls import path

from . import views

urlpatterns = [
    path('index_page/', views.index_page, name='index_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('register/', views.register, name='register')
]