from unittest import result
import pytest

from src.cadastro_veiculo import CadastroVeiculo
from src.veiculo import Veiculo


def test_retorno_inserir():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 'erer')
    cadastro = CadastroVeiculo()

    # Quando / When
    resultado = cadastro.inserir(veiculo)

    # Então / Then
    assert resultado


def test_consultar_veiculo_cadastrado_por_id():
    # Dado / Given
    veiculo = Veiculo('123', 'adasd', 'fadsa')
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('123')

    # Então / Then
    assert resultado.id == '123'


def test_consultar_id_veiculo_inserido():
    # Dado / Given
    veiculo = Veiculo('1345', 'rere', 'erer')
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.id == '1345'


def test_consultar_km_veiculo_inserido():
    # Dado / Given
    veiculo = Veiculo('1345', 'rere', 'erer')
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.km == 'erer'


def test_consultar_placa_veiculo_inserido():
    # Dado / Given
    veiculo = Veiculo('1345', 'rere', 'erer')
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.placa == 'rere'


def test_remover_por_id_veiculo():
    # Dado / Given
    veiculo = Veiculo('1345', 'rere', 'erer')
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.remover_por_id('1345')

    # Então / Then
    assert resultado


def test_validar_remocao_por_id():
    # Dado / Given
    veiculo_a = Veiculo('1321', 'gol', 1263456)
    veiculo_b = Veiculo('4567', 'ABC', 4567)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo_a)
    cadastro.inserir(veiculo_b)
    resultado = cadastro.remover_por_id('1321')

    resultado = cadastro.consultar('1321')

    # Então / Then
    assert resultado is None

