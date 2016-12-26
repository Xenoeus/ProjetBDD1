import SPRJUDToSQL
import sqlite3

class Relation:
   """
   Cette classe represente une relation en SPJRUD ou une table en SQL.
   """
   
   
   def __init__(self, nom):
      self.nom = nom
      self.colonnes = self.relationColonnes(nom);
      self.nomExpression = "Relation("+nom+")"
         
         
   def __str__(self):
      return self.nom

   def verifieTable(self):
      """
      Cette methode verifie si la table utilisee existe bien
      """
      connection = sqlite3.connect(SPRJUDToSQL.dataBase)
      c = connection.cursor()
      c.execute("SELECT name FROM sqlite_master WHERE type='table';")
      for i in c:
         if(i[0]== self.nom):
            connection.close()
            return False

      connection.close()
      return True

   def relationColonnes(self,nom):
      """
      Cette methode cree un tableau avec les nom des colonnes de la relation et leur types
      """
      connection = sqlite3.connect(SPRJUDToSQL.dataBase)
      c = connection.cursor()
      commande = "PRAGMA table_info("+str(nom)+");"
      c.execute(commande)
      colonnes = []
      gollum = c.fetchall()
      for i in gollum:
         detail = [i[1],i[2]]
         colonnes.append(detail)
      return colonnes
