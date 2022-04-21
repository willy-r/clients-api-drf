def validate_name(name: str) -> str:
    """Validates the name field."""
    return name.isalpha()


def validate_cpf(cpf: str) -> str:
    """Validates the cpf field."""
    return len(cpf) == 11


def validate_rg(rg: str) -> str:
    """Validates the rg field."""
    return len(rg) == 9


def validate_cellphone(cellphone: str) -> str:
    """Validates the cellphone field."""
    return not len(cellphone) < 11
