import pytest

from src.cadastro_veiculo import CadastroVeiculo
from src.veiculo import Veiculo


def test_private_veiculo_id_error():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 'erer')

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        veiculo.id = '12345'


def test_private_veiculo_placa_error():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 'erer')

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        veiculo.placa = 'teste'


def test_private_veiculo_km_error():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 'erer')

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        veiculo.km = 1.1
