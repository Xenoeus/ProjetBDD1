from Expression import Expression
from Eq import Eq
from Relation import Relation
from Select import Select
from Project import Project
from Join import Join
from Rename import Rename
from Union import Union
from Difference import Difference
from Attribut import Attribut
from Cst import Cst
import sqlite3

class SPRJUDToSQL():

   def selectDataBase(self, dataBase):
      """
      Cette methode permet de définir la base de donnée utilisée
      """
      self.dataBase = dataBase

   def traduction(self, SPRJUD):
      """
      Cette methode permet de traduire une requête de sprjud en sql elle revoit true si l'opération c'est bien passée et false sinon
      """
      try:
         SPRJUD.print_query()
         return true
      except TypeError as inst:
         print(inst.args)
         return false

   def traductionAndExecution(self, SPRJUD):
      """
      Cette methode permet de traduire et d'executer une requête de sprjud en sql elle revoit true si l'opération c'est bien passée et false sinon
      """
      connection = sqlite3.connect('test.db')
      c = connection.cursor()
      connection.commit()
      
      try:
         stri = SPRJUD.string_query()
         c.execute(stri)
         """
         gollum = c.getColumnNames()
         for i in gollum:
             print(i[1])
         borimir = c.fetchall()
         for i in borimir:
             print(i)
        """
      except TypeError as inst:
         print(inst.args)
         return False
         
      connection.rollback()
      connection.close()
      return True
