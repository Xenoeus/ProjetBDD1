import sqlite3
from Traducteur import *

class SPRJUDToSQL():

   def selectDataBase(self, dataBaseUse):
      """
      Cette methode permet de définir la base de donnée utilisée
      """
      global dataBase
      dataBase = dataBaseUse

   def traduction(self, SPRJUD):
      """
      Cette methode permet de traduire une requête de sprjud en sql elle revoit true si l'opération c'est bien passée et false sinon
      """
      try:
         traducteur = Traducteur()
         print(traducteur.traduction(SPRJUD))
         return True
      except TypeError as inst:
         print(inst.args)
         return False

   def traductionAndExecution(self, SPRJUD):
      """
      Cette methode permet de traduire et d'executer une requête de sprjud en sql elle revoit true si l'opération c'est bien passée et false sinon
      """
      connection = sqlite3.connect(dataBase)
      c = connection.cursor()
      connection.commit()
      
      try:
         traducteur = Traducteur()
         stri = traducteur.traduction(SPRJUD)
         c.execute(stri)
         gollum = c.description
         nomColonne = ""
         for i in gollum:
             nomColonne+=i[0]
         print(nomColonne)
         borimir = c.fetchall()
         for i in borimir:
             print(i)
      except TypeError as inst:
         print(inst.args)
         return False
         
      connection.rollback()
      connection.close()
      return True
