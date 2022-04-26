from rest_framework import serializers
from user.models import Courier
from .models import CourierWeaklyIncome


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = "__all__"


class CourierWeaklyIncomeSerializer(serializers.ModelSerializer):
    courier = CourierSerializer(read_only=True)

    class Meta:
        model = CourierWeaklyIncome
        fields = ["id", "courier", "date", "amount"]
