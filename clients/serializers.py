from rest_framework import serializers
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate_cpf(self, cpf):
        """Validates the cpf field."""
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter exatos 11 dígitos.')
        
        return cpf
