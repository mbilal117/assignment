from rest_framework import serializers

from api.models import Customer, Policy


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PolicySerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all()
    )
    class Meta:
        model = Policy
        fields = ('type', 'premium', 'cover', 'customer')