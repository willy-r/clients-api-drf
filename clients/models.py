from django.db import models

class Client(models.Model):
    """Represents a client."""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    cellphone = models.CharField(max_length=14)
    is_active = models.BooleanField()

    def __str__(self) -> str:
        return self.name
