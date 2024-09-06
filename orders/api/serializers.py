from rest_framework import serializers
from orders.models import Order as DjangoOrderModel

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoOrderModel
        fields = '__all__'
