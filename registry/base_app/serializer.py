from rest_framework import serializers
from .models import Variable, Request


class VariableSerializer(serializers.ModelSerializer):
    """
    Serializer for individual Variable objects
    """
    class Meta:
        model = Variable
        fields = ['id', 'name', 'description', 'collected_datetime',
                  'availability', 'expiration_date']


class RequestSerializer(serializers.ModelSerializer):
    """
    Serializer for Request objects, including nested VariableSerializer
    """
    variables = VariableSerializer(many=True)

    class Meta:
        model = Request
        fields = ['request_id', 'status', 'username', 'contact_email',
                  'variables']
