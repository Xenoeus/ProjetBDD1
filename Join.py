from Relation import Relation
from Expression import Expression

class Join(Expression):
   """
   Cette classe represente la jointure en SPJRUD
   """
    
   def __init__(self, relation1, relation2):
      self.relation1 = relation1
      self.relation2 = relation2
      self.verifieAttributs()
      self.query = "SELECT * FROM "+str(self.relation1)+" NATURAL JOIN "+str(self.relation2)
      changementColonnes(relation1, relation2)
      

   def __str__(self):
      return self.query

   def verifieAttributs(self):
      """
      Cette methode verifie si les valeurs entrees dans le constructeur
      sont bien celles que l'on attend.
      """
      if not isinstance(self.relation1, Relation) and not isinstance(self.relation1, Expression):
         raise TypeError("L'attribut relation1 doit etre un objet de type Relation ou Expression")
      elif not isinstance(self.relation2, Relation) and not isinstance(self.relation2, Expression):
         raise TypeError("L'attribut relation2 doit etre un objet de type Relation ou Expression")


   def changementColonnes(self, relation1 , relation2):
      """
      Cette méthode fais la jointure des colonnes des deux relations
      """
      self.colonnes = []
      colrelation1 = self.relation1
      colrelation2 = self.relation2
      while(len(colrelation1)):
         self.colonnes.append(colrelation1[0])
         colrelation2.remove(colrelation1[0])
         del colrelation1[0]
      for i in colrelation2:
         self.colonnes.append(colrelation2[i])

         
