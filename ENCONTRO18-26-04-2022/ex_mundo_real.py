from abc import ABC, abstractmethod

class Database (ABC):
  
  @abstractmethod
  def connect(self):
    pass
  
class MySQL(Database):
  
  def connect(self):
    print('Conectado ao MySQL')
    
class PostgreSQL(Database):
  
  def connect(self):
    print('Conectado ao PostgreSQL')
    
class SQLServer(Database):
  
  def connect(self):
    print('Conectado ao SQLServer')