def calcular_crescimento(valor_atual, valor_anterior):
    """
    Calcula o crescimento percentual entre dois valores.
    """
    if valor_anterior == 0:
        return 0.0  # Evitar a divisão 0
    
    crescimento = ((valor_atual - valor_anterior) / valor_anterior) * 100
    return crescimento