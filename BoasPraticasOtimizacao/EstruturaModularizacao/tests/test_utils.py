from src.utils import calcular_imc


def test_imc():
  resultado = calcular_imc(102,1.92)
  assert resultado is not None