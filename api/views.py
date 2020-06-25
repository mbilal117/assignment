from django.shortcuts import render
from rest_framework import generics

from api.models import Customer, Policy
from api.serializers import CustomerSerializer, PolicySerializer


class CreateCustomer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CreatePolicy(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
