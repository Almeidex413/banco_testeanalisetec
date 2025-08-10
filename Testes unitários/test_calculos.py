from calculos import calcular_crescimento

def test_crescimento_positivo():
    # 'assert' verifica se a condição é verdadeira. Se não for, o teste falha.
    assert calcular_crescimento(120, 100) == 20.0

def test_crescimento_negativo():
    assert calcular_crescimento(80, 100) == -20.0

def test_sem_crescimento():
    assert calcular_crescimento(100, 100) == 0.0

def test_crescimento_a_partir_de_zero():
    assert calcular_crescimento(50, 0) == 0.0