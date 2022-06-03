from flask import Flask, request

from src.business.cadastro_cliente import CadastroCliente

teste = Flask(__name__)

# Definir a rota - ex: www.site.com.br/rota, colocar "/rota". Nesse caso, sendo a homme, vai diretamente "/"

@teste.route("/")
def hello_world():
  return "<p>Hello World!</p>"

@teste.route("/stone", methods=['POST'])
def stone():
  return "stone codigo's!"

@teste.route("/stone", methods=['PUT'])
def atualizar():
  return "stone codigo's!"

@teste.route("/veiculo", methods=['DELETE'])
def deletar_veiculo():
  return "stone codigo's!" 