from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page for the destinations app
    path('<int:pk>/', views.destination_detail, name='destination_detail'),  # Detail page
]
