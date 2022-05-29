import pytest
from src.entity import Entity

from src.veiculo import Veiculo


def test_private_veiculo_id_error():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 1234)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        veiculo.id = '12345'


def test_private_veiculo_placa_error():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 12234)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        veiculo.placa = 'teste'


def test_private_veiculo_km_error():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 124674)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        veiculo.km = 1.1

def test_tipo_veiculo_id():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 1234)
    
    # Quando / When

    # Então / Then
    assert type(veiculo.id) == str
    
def test_tipo_veiculo_placa():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 1234)
    
    # Quando / When

    # Então / Then
    assert type(veiculo.placa) == str

def test_tipo_veiculo_km():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 1234)
    
    # Quando / When

    # Então / Then
    assert type(veiculo.km) == float
    
def test_tipo_veiculo_id_error():
    # Dado / Given
    
    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        veiculo = Veiculo(124, 'rere', 1234)
        
def test_tipo_veiculo_placa_error():
    # Dado / Given
    
    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        veiculo = Veiculo('rere', 1234, 1234)

def test_tipo_veiculo_km_error():
    # Dado / Given
    
    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        veiculo = Veiculo('rere', 'areare', 'abcd')
        
def test_classe_veiculo():
    # Dado / Given
    veiculo = Veiculo('rere', 'abcd', 1234)
    
    # Quando / When
    
    # Então / Then
    assert isinstance(veiculo, Veiculo)
    
def test_superclasse_veiculo_entity():
    # Dado / Given
    veiculo = Veiculo('rere', 'abcd', 1234)
    
    # Quando / When
    
    # Então / Then
    assert isinstance(veiculo, Entity)