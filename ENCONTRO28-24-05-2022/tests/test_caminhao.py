import pytest

from src.caminhao import Caminhao
from src.entity import Entity
from src.veiculo import Veiculo


def test_private_caminhao_id_error():
    # Dado / Given
    caminhao = Caminhao('123', 'rere', 1234, 127)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        caminhao.id = '12345'


def test_private_caminhao_placa_error():
    # Dado / Given
    caminhao = Caminhao('123', 'rere', 1237, 127.5)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        caminhao.placa = 'teste'


def test_private_caminhao_km_error():
    # Dado / Given
    caminhao = Caminhao('123', 'rere', 1247, 12476)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        caminhao.km = 1.1


def test_private_caminhao_carga_error():
    # Dado / Given
    caminhao = Caminhao('123', 'rere', 1247, 12476)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        caminhao.carga = 1.1


def test_tipo_caminhao_id():
    # Dado / Given
    caminhao = Caminhao('123', 'rere', 1234, 1247)

    # Quando / When

    # Então / Then
    assert type(caminhao.id) == str


def test_tipo_caminhao_placa():
    # Dado / Given
    caminhao = Caminhao('123', 'rere', 1234, 1274)

    # Quando / When

    # Então / Then
    assert type(caminhao.placa) == str


def test_tipo_caminhao_km():
    # Dado / Given
    caminhao = Caminhao('123', 'rere', 1234, 1247)

    # Quando / When

    # Então / Then
    assert type(caminhao.km) == float


def test_tipo_caminhao_carga():
    # Dado / Given
    caminhao = Caminhao('123', 'rere', 1234, 1247)

    # Quando / When

    # Então / Then
    assert type(caminhao.carga) == float


def test_tipo_caminhao_id_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        caminhao = Caminhao(124, 'rere', 1234, 1274)


def test_tipo_caminhao_placa_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        caminhao = Caminhao('rere', 1234, 1234, 1247)


def test_tipo_caminhao_km_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        caminhao = Caminhao('rere', 'areare', 'abcd', 1247)


def test_tipo_caminhao_carga_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        caminhao = Caminhao('rere', 'areare', 1234, 'abcd')


def test_classe_caminhao():
    # Dado / Given
    caminhao = Caminhao('rere', 'abcd', 1234, 12347)

    # Quando / When

    # Então / Then
    assert isinstance(caminhao, Caminhao)


def test_superclasse_caminhao_veiculo():
    # Dado / Given
    caminhao = Caminhao('rere', 'abcd', 1234, 12474)

    # Quando / When

    # Então / Then
    assert isinstance(caminhao, Veiculo)

def test_superclasse_caminhao_entity():
    # Dado / Given
    caminhao = Caminhao('rere', 'abcd', 1234, 1527)
    
    # Quando / When
    
    # Então / Then
    assert isinstance(caminhao, Entity)