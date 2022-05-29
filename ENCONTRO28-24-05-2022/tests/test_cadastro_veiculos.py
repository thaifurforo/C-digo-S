import pytest

from src.automovel import Automovel
from src.cadastro_veiculo import CadastroVeiculo
from src.caminhao import Caminhao
from src.veiculo import Veiculo


def test_retorno_inserir():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 754.3)
    cadastro = CadastroVeiculo()

    # Quando / When
    resultado = cadastro.inserir(veiculo)

    # Então / Then
    assert resultado


def test_consultar_veiculo_cadastrado_por_id():
    # Dado / Given
    veiculo = Veiculo('123', 'adasd', 12345)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('123')

    # Então / Then
    assert resultado.id == '123'


def test_consultar_id_veiculo_inserido():
    # Dado / Given
    veiculo = Veiculo('1345', 'rere', 46321)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.id == '1345'


def test_consultar_km_veiculo_inserido():
    # Dado / Given
    veiculo = Veiculo('1345', 'rere', 512.4)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.km == 512.4


def test_consultar_placa_veiculo_inserido():
    # Dado / Given
    veiculo = Veiculo('1345', 'rere', 1264.7)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.placa == 'rere'


def test_remover_por_id_veiculo():
    # Dado / Given
    veiculo = Veiculo('1345', 'rere', 46474.5)
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


def test_validar_remocao_por_entidade():
    # Dado / Given
    veiculo_a = Veiculo('1321', 'gol', 1263456)
    veiculo_b = Veiculo('4567', 'ABC', 4567)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo_a)
    cadastro.inserir(veiculo_b)
    resultado = cadastro.remover_por_entidade(veiculo_a)

    resultado = cadastro.consultar('1321')

    # Então / Then
    assert resultado is None


def test_listar_todos():
    # Dado / Given
    veiculo_a = Veiculo('1321', 'gol', 1263456)
    veiculo_b = Veiculo('4567', 'ABC', 4567)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo_a)
    cadastro.inserir(veiculo_b)
    resultado = cadastro.listar_todos(cadastro)

    # Então / Then
    assert len(resultado) == 2


def test_consultar_caminhao_cadastrado_por_id():
    # Dado / Given
    caminhao = Caminhao('123', 'adasd', 17742, 1200)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(caminhao)
    resultado = cadastro.consultar('123')

    # Então / Then
    assert resultado.id == '123'


def test_consultar_id_caminhao_inserido():
    # Dado / Given
    caminhao = Caminhao('1345', 'rere', 12467, 4578)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(caminhao)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.id == '1345'


def test_consultar_km_caminhao_inserido():
    # Dado / Given
    caminhao = Caminhao('1345', 'rere', 124.7, 16467)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(caminhao)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.km == 124.7


def test_consultar_placa_caminhao_inserido():
    # Dado / Given
    veiculo = Caminhao('1345', 'rere', 1217.5, 164664)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.placa == 'rere'


def test_consultar_carga_caminhao_inserido():
    # Dado / Given
    veiculo = Caminhao('1345', 'rere', 1217.5, 164664)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.carga == 164664


def test_remover_por_id_caminhao():
    # Dado / Given
    caminhao = Caminhao('1345', 'rere', 567541, 16467)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(caminhao)
    resultado = cadastro.remover_por_id('1345')

    # Então / Then
    assert resultado


def test_validar_remocao_por_id_caminhao():
    # Dado / Given
    caminhao_a = Caminhao('1321', 'gol', 1263456, 12345)
    caminhao_b = Caminhao('4567', 'ABC', 4567, 1546.8)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(caminhao_a)
    cadastro.inserir(caminhao_b)
    resultado = cadastro.remover_por_id('1321')

    resultado = cadastro.consultar('1321')

    # Então / Then
    assert resultado is None


def test_validar_remocao_por_entidade_caminhao():
    # Dado / Given
    caminhao_a = Caminhao('1321', 'gol', 1263456, 1234)
    caminhao_b = Caminhao('4567', 'ABC', 4567, 1248.5)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(caminhao_a)
    cadastro.inserir(caminhao_b)
    resultado = cadastro.remover_por_entidade(caminhao_b)

    resultado = cadastro.consultar('4567')

    # Então / Then
    assert resultado is None
    

def test_consultar_automovel_cadastrado_por_id():
    # Dado / Given
    automovel = Automovel('123', 'adasd', 17742, 40, 5)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(automovel)
    resultado = cadastro.consultar('123')

    # Então / Then
    assert resultado.id == '123'


def test_consultar_id_automovel_inserido():
    # Dado / Given
    automovel = Automovel('1345', 'rere', 12467, 40, 5)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(automovel)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.id == '1345'


def test_consultar_km_automovel_inserido():
    # Dado / Given
    automovel = Automovel('1345', 'rere', 124.7, 40, 5)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(automovel)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.km == 124.7


def test_consultar_placa_automovel_inserido():
    # Dado / Given
    automovel = Automovel('1345', 'rere', 1217.5, 40, 5)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(automovel)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.placa == 'rere'


def test_consultar_bagageiro_automovel_inserido():
    # Dado / Given
    automovel = Automovel('1345', 'rere', 1217.5, 40, 5)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(automovel)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.bagageiro == 40

def test_consultar_portas_automovel_inserido():
    # Dado / Given
    automovel = Automovel('1345', 'rere', 1217.5, 40, 5)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(automovel)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.portas == 5

def test_remover_por_id_automovel():
    # Dado / Given
    automovel = Automovel('1345', 'rere', 567541, 40, 5)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(automovel)
    resultado = cadastro.remover_por_id('1345')

    # Então / Then
    assert resultado


def test_validar_remocao_por_id_automovel():
    # Dado / Given
    automovel_a = Automovel('1321', 'gol', 1263456, 40, 5)
    automovel_b = Automovel('4567', 'ABC', 4567, 20, 3)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(automovel_a)
    cadastro.inserir(automovel_b)
    resultado = cadastro.remover_por_id('1321')

    resultado = cadastro.consultar('1321')

    # Então / Then
    assert resultado is None


def test_validar_remocao_por_entidade_automovel():
    # Dado / Given
    automovel_a = Automovel('1321', 'gol', 1263456, 40, 5)
    automovel_b = Automovel('4567', 'ABC', 4567, 20, 3)
    cadastro = CadastroVeiculo()

    # Quando / When
    cadastro.inserir(automovel_a)
    cadastro.inserir(automovel_b)
    resultado = cadastro.remover_por_entidade(automovel_b)

    resultado = cadastro.consultar('4567')

    # Então / Then
    assert resultado is None

def test_private_lista():
    # Dado / Given
    veiculo = Veiculo('123', 'rere', 1234)

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        veiculo.id = '12345'
