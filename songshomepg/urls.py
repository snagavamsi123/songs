from django.urls import path
from songshomepg import views

urlpatterns = [
    path('', views.home),
]