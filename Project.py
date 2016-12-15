from Expression import Expression
from Attribut import Attribut
from Relation import Relation

class Project(Expression):

   """
   Cette classe represente la projection en SPJRUD.
   """
   def __init__(self, attributs, relation): 
      self.attributs = attributs
      self.relation = relation
      self.verifieAttributs()
      self.query = "SELECT "+str(self.attributs)+" FROM "+str(self.relation)

   def __str__(self):
      return self.query

   def verifieAttributs(self):
      """
      Cette methode verifie si les valeurs entrees dans le constructeur
      sont bien celles que l'on attend.
      """
      if not isinstance(self.attributs, list) or len(self.attributs) == 0:
         raise TypeError("Le premier attribut de Project doit etre une liste non vide d'objets Attribut")
      elif not isinstance(self.relation, Relation) and not isinstance(self.relation, Expression):
         raise TypeError("Le second attribut de Project doit etre un objet de type Relation ou Expression")
      else:
         for e in self.attributs:
            if not isinstance(self.attributs[e], Attribut):
               raise TypeError("Les elements de la liste du premier attribut de Project doivent etre de type Attribut")
