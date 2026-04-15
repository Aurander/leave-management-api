from rest_framework import serializers
from .models import LeaveRequest


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'
        read_only_fields = ['user', 'status']

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "Start date must be before end date")
        return data
