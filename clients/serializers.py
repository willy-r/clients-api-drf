from rest_framework import serializers
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    
    def validate_name(self, name: str) -> str:
        """Validates the name field."""
        if not name.isalpha():
            raise serializers.ValidationError('Nome só pode conter caracteres alfabéticos.')
        
        return name
    
    def validate_cpf(self, cpf: str) -> str:
        """Validates the cpf field."""
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter exatos 11 dígitos.')
        
        return cpf
    
    def validate_rg(self, rg: str) -> str:
        """Validates the rg field."""
        if len(rg) != 9:
            raise serializers.ValidationError('O RG deve conter exatos 9 dígitos.')
        
        return rg

    def validate_cellphone(self, cellphone: str) -> str:
        """Validates the cellphone field."""
        if len(cellphone) < 11:
            raise serializers.ValidationError('O celular deve ter no mínimo 11 dígitos.')
        
        return cellphone
