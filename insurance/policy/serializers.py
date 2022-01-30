from .models import Policy
from rest_framework import serializers
from django.core.exceptions import ValidationError


class PolicySerializer(serializers.ModelSerializer):
    Premium = serializers.IntegerField()
    Customer_id = serializers.IntegerField()
    Policy_id = serializers.IntegerField()
    Date_of_Purchase = serializers.DateField(format='%m/%d/%Y')

    def validate_Premium(self, value):
        """
        Check that value is a valid name.
        """
        # Premium value must be less than the 1000000 (1M)
        if not value <= 1000000:
            raise ValidationError(" Invalid data. Premium Must be less then '1000000'")
        return value

    class Meta:
        model = Policy
        fields = '__all__'
        # Date_of_Purchase only read we can't update this filed
        read_only_fields = ['Date_of_Purchase']


