from src.cadastro_abstract import CadastroAbstract
from src.entity import Entity


def test_retorno_inserir():
    # Dado / Given
    entity = Entity('123')
    cadastro = CadastroAbstract()

    # Quando / When
    resultado = cadastro.inserir(entity)

    # Então / Then
    assert resultado


def test_consultar_entity_cadastrado_por_id():
    # Dado / Given
    entity = Entity('123')
    cadastro = CadastroAbstract()

    # Quando / When
    cadastro.inserir(entity)
    resultado = cadastro.consultar('123')

    # Então / Then
    assert resultado.id == '123'


def test_consultar_id_entity_inserido():
    # Dado / Given
    entity = Entity('1345')
    cadastro = CadastroAbstract()

    # Quando / When
    cadastro.inserir(entity)
    resultado = cadastro.consultar('1345')

    # Então / Then
    assert resultado.id == '1345'


def test_remover_por_id_entity():
    # Dado / Given
    entity = Entity('1345')
    cadastro = CadastroAbstract()

    # Quando / When
    cadastro.inserir(entity)
    resultado = cadastro.remover_por_id('1345')

    # Então / Then
    assert resultado


def test_validar_remocao_por_id():
    # Dado / Given
    entity_a = Entity('1321')
    entity_b = Entity('4567')
    cadastro = CadastroAbstract()

    # Quando / When
    cadastro.inserir(entity_a)
    cadastro.inserir(entity_b)
    resultado = cadastro.remover_por_id('1321')

    resultado = cadastro.consultar('1321')

    # Então / Then
    assert resultado is None


def test_validar_remocao_por_entidade():
    # Dado / Given
    entity_a = Entity('1321')
    entity_b = Entity('4567')
    cadastro = CadastroAbstract()

    # Quando / When
    cadastro.inserir(entity_a)
    cadastro.inserir(entity_b)
    resultado = cadastro.remover_por_entidade(entity_a)

    resultado = cadastro.consultar('1321')

    # Então / Then
    assert resultado is None


def test_listar_todos():
    # Dado / Given
    entity_a = Entity('1321')
    entity_b = Entity('4567')
    cadastro = CadastroAbstract()

    # Quando / When
    cadastro.inserir(entity_a)
    cadastro.inserir(entity_b)
    resultado = cadastro.listar_todos(cadastro)

    # Então / Then
    assert len(resultado) == 2
