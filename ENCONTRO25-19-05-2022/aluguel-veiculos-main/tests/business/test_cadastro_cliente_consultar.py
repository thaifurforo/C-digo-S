from unittest import TestCase
from src.entities.cliente import Cliente
from src.business.cadastro_cliente import CadastroCliente
from src.exceptions.cliente_not_found_error import ClienteNotFoundError


class TestCadastroClienteConsultar(TestCase):

    #def __init__(self):

    #def SetUp(self):

    def test_consulta_cliente_id(self):
        # dado
        cliente_a = Cliente('10', 'Rua Teste, 550', '99871-2403', 'Monique')
        cliente_b = Cliente('20', 'Rua Jose, 50', '99565-2403', 'Matheus')
        cadastro = CadastroCliente()
        
        # quando
        cadastro.inserir(cliente_a)
        cadastro.inserir(cliente_b)
        resultado_a = cadastro.consultar('10')
        resultado_b = cadastro.consultar('20')
        
        # então
        self.assertIsInstance(cliente_a, Cliente)
        self.assertIsInstance(cliente_b, Cliente)
        self.assertEqual(resultado_a.id, '10')
        self.assertEqual(resultado_b.id, '20')
        
    def test_consulta_cliente_erro(self):
        # dado
        cliente_a = Cliente('10', 'Rua Teste, 550', '99871-2403', 'Monique')
        cliente_b = Cliente('20', 'Rua Jose, 50', '99565-2403', 'Matheus')
        cadastro = CadastroCliente()
        
        # quando
        cadastro.inserir(cliente_a)
        cadastro.inserir(cliente_b)
        
        # então
        with self.assertRaises(ClienteNotFoundError):
            cadastro.consultar('40')
        
        
