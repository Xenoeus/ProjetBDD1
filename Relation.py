import sqlite3
class Relation:
   """
   Cette classe represente une relation en SPJRUD ou une table en SQL.
   """

   def verification(self,nom):
      connection = sqlite3.connect('test.db')
      c = connection.cursor()
      c.execute("SELECT name FROM sqlite_master WHERE type='table';")
      for i in c:
         if(i[0]== nom):
            connection.close()
            return False

      connection.close()
      return True
   
   def __init__(self, nom, attributs):
      self.nom = nom
      self.attributs = attributs
      if (self.verification(nom)):
         print(nom)
         print("Ce nom de relation n'est pas correct ou cette relation n'existe pas")
   def __str__(self):
      return self.nom


