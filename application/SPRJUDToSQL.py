import sqlite3
from Traducteur import *

class SPRJUDToSQL():

   def selectionDataBase(self, dataBaseUse):
      """
      Cette methode permet de définir la base de donnée utilisée
      """
      global dataBase
      dataBase = dataBaseUse

   def traduction(self, SPRJUD):
      """
      Cette methode permet de traduire une requête de sprjud en sql. Elle revoit true si l'opération c'est bien passée et false sinon
      """
      try:
         traducteur = Traducteur()
         print(traducteur.traduction(SPRJUD).string_query())
         return True
      except TypeError as inst:
         print(inst.args)
         return False

   def traductionEtExecution(self, SPRJUD):
      """
      Cette methode permet de traduire et d'executer une requête de sprjud en sql. Elle revoit true si l'opération c'est bien passée et false sinon
      """
      connection = sqlite3.connect(dataBase)
      c = connection.cursor()
      connection.commit()
      
      try:
         traducteur = Traducteur()
         stri = traducteur.traduction(SPRJUD).string_query()
         print(stri)
         c.execute(stri)
         gollum = c.description
         nomColonne = "|"
         for i in gollum:
             nomColonne+=i[0]+"|"
         print(nomColonne)
         borimir = c.fetchall()
         for i in borimir:
            stan = "|"
            for j in i:
                stan += str(j) +"|"
            print(stan)
      except TypeError as inst:
         connection.rollback()
         connection.close()
         print(inst.args)
         return False
         
      connection.rollback()
      connection.close()
      return True

   def traductionEtCreationDeTable(self, SPRJUD, nom): 
      """
      Cette methode permet de traduire et d'executer une requête de sprjud en sql et de créer une nouvelle table avec le resultat. Elle revoit true si l'opération c'est bien passée et false sinon
      """
      connection = sqlite3.connect(dataBase)
      c = connection.cursor()
      connection.commit()
      
      try:
         traducteur = Traducteur()
         requete = traducteur.traduction(SPRJUD)
         stri = requete.string_query()
         print(stri)
         c.execute(stri)
         gollum = c.description
         nomColonne = "|"
         for i in gollum:
             nomColonne+=i[0]+"|"
         print(nomColonne)
         borimir = c.fetchall()
         for i in borimir:
            stan = "|"
            for j in i:
                stan += str(j) +"|"
            print(stan)
         newcolonnes = ""
         for i in requete.colonnes:
            newcolonnes += " "+i[0] +" "+ i[1]+","
         newcolonnes = newcolonnes[:len(newcolonnes)-1]
         creation = '''CREATE TABLE '''+ nom +'''('''+newcolonnes+''')'''
         c.execute(creation)
         for i in borimir:
            insert = "INSERT INTO "+nom+" VALUES " + str(i)
            c.execute(insert)

      except TypeError as inst:
         connection.rollback()
         connection.close()
         print(inst.args)
         return False
         
      connection.commit()
      connection.close()
      return True

