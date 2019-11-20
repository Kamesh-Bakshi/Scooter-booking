from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rideapp.models import scooters

class scootersSerializer(serializers.ModelSerializer):

    class Meta:
        model = scooters
        fields = '__all__'

class BookScooterSerializer(serializers.Serializer):

    uniqueid = serializers.IntegerField()
    def verify(self,data):
        uniqueid = data.get("uniqueid")
        if not uniqueid:
            raise ValidationError("Scooter number is required")
        try:
            rider= scooters.objects.get(uniqueid=uniqueid)
        except scooters.DoesNotExist:
            raise ValidationError("Scooter not exists")

        return data