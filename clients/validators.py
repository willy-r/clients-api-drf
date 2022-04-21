import re

from validate_docbr import CPF


def validate_name(name: str) -> str:
    """Validates the name field."""
    return name.isalpha()


def validate_cpf(cpf_user: str) -> str:
    """Validates the cpf field.
    
    Example: 01234567890
    """
    cpf = CPF()
    return cpf.validate(cpf_user)


def validate_rg(rg: str) -> str:
    """Validates the rg field."""
    return len(rg) == 9


def validate_cellphone(cellphone: str) -> str:
    """Validates the cellphone field.
    
    Example: 11 91234-1234
    """
    pattern = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    return re.findall(pattern, cellphone)
