from django.db import models


class Client(models.Model):
    """Represents a Client."""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    cellphone = models.CharField(max_length=14, unique=True)
    is_active = models.BooleanField('Ativo?', null=False, blank=False, default=True)

    def __str__(self) -> str:
        return self.name
