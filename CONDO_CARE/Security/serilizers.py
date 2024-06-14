from rest_framework import serializers


class Emergencyserializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    EMERGENCY_TYPES = [
        ('fire', 'Fire'),
        ('medical', 'Medical Emergency'),
        ('security', 'Security Threat'),
    ]

    emergency_type = serializers.ChoiceField(choices=EMERGENCY_TYPES)
    emergency_details = serializers.CharField()
    notify_email = serializers.BooleanField(default=False)
    created_at  = serializers.DateTimeField(read_only=True)

class VisitorRegistrationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=64)
    tenant_name = serializers.CharField(max_length=64)
    floor_number = serializers.IntegerField()
    unit_number = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=64)
    home_address = serializers.CharField()
    reason_to_visit = serializers.CharField()
    
    TOWER_CHOICES = [
        ('Tower 1', 'Tower 1'),
        ('Tower 2', 'Tower 2'),
        ('Tower 3', 'Tower 3'),
        ('others', 'Others'),
    ]
    
    tower_select = serializers.ChoiceField(choices=TOWER_CHOICES)
    datetime_local = serializers.DateTimeField()
    