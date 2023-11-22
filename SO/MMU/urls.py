from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('process_json/', views.process_json, name='process_json'),
]
