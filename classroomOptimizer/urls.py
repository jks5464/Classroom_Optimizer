from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='classroom-home'),
    path('about/', views.about, name='classroom-about')
]