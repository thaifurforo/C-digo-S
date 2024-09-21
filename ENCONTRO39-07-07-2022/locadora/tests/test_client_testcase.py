from django.test import TestCase
from rest_framework.test import APIClient
from locadora.models.cliente import Cliente


class ClienteTestCase(TestCase):

  def test_cliente_post_sucesso(self):
    # given
    cliente = {"nome": "maicon"}

    # when
    client = APIClient()
    response = client.post('/cliente/', cliente, format='json')

    # then
    self.assertEqual(response.status_code, 201)


  def test_cliente_post_error(self):
      # given
      cliente = {"nome": "maicon francisco"}

      # when
      client = APIClient()
      response = client.post('/cliente/', cliente, format='json')

      # then
      self.assertEqual(response.status_code, 400)


  def test_cliente_create(self):
    # given
    Cliente.objects.create(nome='Maicon')

    # when
    cliente = Cliente.objects.get(nome='Maicon Francisco')

    # then
    self.assertEqual(cliente.nome, 'Maicon Francisco')