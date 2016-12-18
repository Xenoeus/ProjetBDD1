from Expression import *
from Eq import *
from Relation import *
from Select import *
from Project import *
from Join import *
from Rename import *
from Union import *
from Difference import *
from Attribut import *
from Cst import *
import sqlite3

class SPRJUDToSQL():

   def selectDataBase(self, dataBase):
      self.dataBase = dataBase

   def traduction(self, SPRJUD):
      try:
         SPRJUD.print_query()
         return true
      except TypeError as inst:
         print(inst.args)
         return false

   def traductionAndExecution(self, SPRJUD):
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
