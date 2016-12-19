from SPRJUDToSQL import *
import sqlite3

class Relation:
   """
   Cette classe represente une relation en SPJRUD ou une table en SQL.
   """
   
   
   def __init__(self, nom, attributs):
      self.nom = nom
      self.attributs = attributs
      if (self.verifieTable(nom)):
         raise TypeError("Ce nom de relation n'est pas correct ou cette relation n'existe pas :\"" + nom + "\"")
      self.colonnes = self.relationColonnes(nom);
      
         
         
   def __str__(self):
      return self.nom

   def verifieTable(self,nom):
      """
      Cette methode verifie si la table utilisee existe bien
      """
      connection = sqlite3.connect('test.db')
      c = connection.cursor()
      c.execute("SELECT name FROM sqlite_master WHERE type='table';")
      for i in c:
         if(i[0]== nom):
            connection.close()
            return False

      connection.close()
      return True

   def relationColonnes(self,nom):
      """
      Cette methode cree un tableau avec les nom des colonnes de la relation
      """
      print("first relation")
      connection = sqlite3.connect('test.db')
      c = connection.cursor()
      commande = "PRAGMA table_info("+str(nom)+");"
      c.execute(commande)
      colonnes = []
      gollum = c.fetchall()
      for i in gollum:
         colonnes.append(i[1])
      return colonnes
