import pytest

from src.entity import Entity


def test_private_entity_id_error():
    # Dado / Given
    entity = Entity('123')

    # Quando / When

    # Então / Then
    with pytest.raises(AttributeError):
        entity.id = '12345'


def test_tipo_entity_id():
    # Dado / Given
    entity = Entity('123')

    # Quando / When

    # Então / Then
    assert type(entity.id) == str


def test_tipo_entity_id_error():
    # Dado / Given

    # Quando / When

    # Então / Then
    with pytest.raises(TypeError):
        entity = Entity(124)


def test_classe_entity():
    # Dado / Given
    entity = Entity('1245')

    # Quando / When

    # Então / Then
    assert isinstance(entity, Entity)
