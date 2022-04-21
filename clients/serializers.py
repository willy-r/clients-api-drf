from rest_framework import serializers
from clients.models import Client
from clients import validators


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        """Validates data."""
        if not validators.validate_name(data['name']):
            raise serializers.ValidationError(
                {'name': 'Nome só pode conter caracteres alfabéticos.'})
        
        if not validators.validate_cpf(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': 'O CPF digitado é inválido.'})

        if not validators.validate_rg(data['rg']):
            raise serializers.ValidationError(
                {'rg': 'O RG deve conter exatos 9 dígitos.'})
        
        if not validators.validate_cellphone(data['cellphone']):
            raise serializers.ValidationError(
                {'cellphone': 'O celular deve estar no seguinte formato: 11 91111-1111'})
        
        return data
