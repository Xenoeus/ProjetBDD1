from Relation import Relation
from Expression import Expression

class Difference(Expression):
   """
   Cette classe represente la difference en SPJRUD
   """
    
   def __init__(self, relation1, relation2):
      self.relation1 = relation1
      self.relation2 = relation2
      self.colonnes = relation1.colonnes
      self.nomExpression = "Difference("+relation1.nomExpression+","+relation2.nomExpression+")"

   def autorisation(self):
      if isinstance(self.relation1, Expression):
         self.relation1.autorisation()
      if isinstance(self.relation2, Expression):
         self.relation2.autorisation()
      if isinstance(self.relation1, Relation):
         if (self.relation1.verifieTable()):
            raise TypeError("Ce nom de relation n'est pas correct ou cette relation n'existe pas :\"" + self.relation1.nom + "\"")
      if isinstance(self.relation2, Relation):
         if (self.relation2.verifieTable()):
            raise TypeError("Ce nom de relation n'est pas correct ou cette relation n'existe pas :\"" + self.relation2.nom + "\"")
      self.verifieAttributs(self.relation1, self.relation2)
      self.query = "SELECT * FROM "+str(self.relation1)+" MINUS SELECT * FROM "+str(self.relation2)

   def __str__(self):
      return self.query

   def verifieAttributs(self, relation1, relation2):
      """
      Cette methode verifie si les valeurs entrees dans le constructeur
      sont bien celles que l'on attend.
      """
      if not isinstance(self.relation1, Relation) and not isinstance(self.relation1, Expression):
         raise TypeError("L'attribut relation1 doit etre un objet de type Relation ou Expression")
      elif not isinstance(self.relation2, Relation) and not isinstance(self.relation2, Expression):
         raise TypeError("L'attribut relation2 doit etre un objet de type Relation ou Expression")
      if(len(relation1.colonnes) != len(relation2.colonnes)):
         raise TypeError("Les deux expression(s)/relation(s) de : Difference(" + self.relation1.nomExpression + "," + self.relation2.nomExpression + ") , doivent avoir le même nombre de colonnes")
      for i in range(len(self.relation1.colonnes)):
         if(self.relation1.colonnes[i][1]!=self.relation2.colonnes[i][1]):
            raise TypeError("Les deux expression(s)/relation(s) de : Difference(" + self.relation1.nomExpression + "," + self.relation2.nomExpression + ") , doivent avoir le même types de colonnes \n La colonnes:"+ self.relation1.colonnes[i][0] +" du type: "+self.relation1.colonnes[i][1]+" et la colonnes:"+ self.relation2.colonnes[i][0] +" du type: "+self.relation2.colonnes[i][1]+" ne sont pas du même type")

