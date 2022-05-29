import pytest

from src.automovel import Automovel
from src.entity import Entity
from src.veiculo import Veiculo


def test_private_automovel_id_error():
    # Dado / Given
    automovel = Automovel('123', 'rere', 1234, 40, 5)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        automovel.id = '12345'


def test_private_automovel_placa_error():
    # Dado / Given
    automovel = Automovel('123', 'rere', 1237, 40, 5)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        automovel.placa = 'teste'


def test_private_automovel_km_error():
    # Dado / Given
    automovel = Automovel('123', 'rere', 1247, 40, 5)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        automovel.km = 1.1


def test_private_automovel_bagageiro_error():
    # Dado / Given
    automovel = Automovel('123', 'rere', 1247, 40, 5)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        automovel.bagageiro = 30


def test_tipo_automovel_id():
    # Dado / Given
    automovel = Automovel('123', 'rere', 1234, 40, 5)

    # Quando / When

    # Então / Then
    assert type(automovel.id) == str


def test_tipo_automovel_placa():
    # Dado / Given
    automovel = Automovel('123', 'rere', 1234, 40, 5)

    # Quando / When

    # Então / Then
    assert type(automovel.placa) == str


def test_tipo_automovel_km():
    # Dado / Given
    automovel = Automovel('123', 'rere', 1234, 40, 5)

    # Quando / When

    # Então / Then
    assert type(automovel.km) == float


def test_tipo_automovel_bagageiro():
    # Dado / Given
    automovel = Automovel('123', 'rere', 1234, 40, 5)

    # Quando / When

    # Então / Then
    assert type(automovel.bagageiro) == int


def test_tipo_automovel_portas():
    # Dado / Given
    automovel = Automovel('123', 'rere', 1234, 40, 5)

    # Quando / When

    # Então / Then
    assert type(automovel.portas) == int


def test_tipo_automovel_id_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        automovel = Automovel(124, 'rere', 1234, 40, 5)


def test_tipo_automovel_placa_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        automovel = Automovel('rere', 1234, 1234, 40, 5)


def test_tipo_automovel_km_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        automovel = Automovel('rere', 'areare', 'abcd', 40, 5)


def test_tipo_automovel_bagageiro_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        automovel = Automovel('rere', 'areare', 1234, 'abcd', 5)


def test_tipo_automovel_portas_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        automovel = Automovel('rere', 'areare', 1234, 40, 'abcd')


def test_classe_automovel():
    # Dado / Given
    automovel = Automovel('rere', 'abcd', 1234, 40, 5)

    # Quando / When

    # Então / Then
    assert isinstance(automovel, Automovel)


def test_superclasse_automovel_veiculo():
    # Dado / Given
    automovel = Automovel('rere', 'abcd', 1234, 40, 5)

    # Quando / When

    # Então / Then
    assert isinstance(automovel, Veiculo)

def test_superclasse_automovel_entity():
    # Dado / Given
    automovel = Automovel('rere', 'abcd', 1234, 40, 5)    
    
    # Quando / When
    
    # Então / Then
    assert isinstance(automovel, Entity)