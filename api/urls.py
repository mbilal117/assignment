from django.urls import path

from api import views

urlpatterns = [
    path('create_customer/', views.CreateCustomer.as_view()),
    path('create_policy/', views.CreatePolicy.as_view()),
]
