from Expression import Expression
from Eq import Eq
from Relation import Relation
from Attribut import Attribut

class Select(Expression):
   """
   Cette classe represente la selection en SPJRUD.
   """

   def __init__(self, egalite, relation):
      self.egalite = egalite
      self.relation = relation
      self.colonnes = self.relation.colonnes
      self.nomExpression = "Select("+ egalite.nomExpression+","+relation.nomExpression+")"


   def autorisation(self):
      """
      Cette methode verifie que toutes les conditions sont respectee, après cela elle traduis l'expression.
      """
      if isinstance(self.relation, Expression):
         self.relation.autorisation()
      if isinstance(self.relation, Relation):
         if (self.relation.verifieTable()):
            raise TypeError("Ce nom de relation n'est pas correct ou cette relation n'existe pas :\"" + self.relation.nom + "\"")
      if (isinstance(self.egalite.attribut1, Attribut)):
         if not(self.verifieColonnes(self.egalite.attribut1.nom)):
            raise TypeError("Ce nom de colonnes n'est pas correct ou n'existe pas :\"" + self.egalite.attribut1.nom + "\"")
      if (isinstance(self.egalite.attribut2, Attribut)):
         if not(self.verifieColonnes(self.egalite.attribut2.nom)):
            raise TypeError("Ce nom de colonnes n'est pas correct ou n'existe pas :\"" + self.egalite.attribut2.nom + "\"")
      if ((isinstance(self.egalite.attribut1, Attribut))and(isinstance(self.egalite.attribut2, Attribut))):
           if(self.recupererType(self.egalite.attribut1.nom)==self.recupererType(self.egalite.attribut2.nom)):
              raise TypeError("Dans "+self.nomExpression+", le type de colonne de "+self.egalite.attribut1.nom+ " du type:"+self.recupererType(self.egalite.attribut1.nom)+" est different du type de colonne de "+self.egalite.attribut2.nom+ " du type:"+self.recupererType(self.egalite.attribut2.nom))
      self.query = "SELECT * FROM "+str(self.relation)+" WHERE "+str(self.egalite)
         
   def __str__(self):
      return self.query

   def verifieColonnes(self, nom):
      """
      Cette methode verifie qu'une colonne existe dans la relation/ l'expression donnee. Elle retourne True si elle existe false sinon
      """
      for i in self.relation.colonnes:
         if(nom == i[0]):
            return True
      return False

   def recupererType(self, nom):
      """
      Cette methode recupere et renvoit le type d'une colonne.
      """
      for i in self.relation.colonnes:
         if(nom == i[0]):
            return i[1]

   def verifieAttributs(self):
      """
      Cette methode verifie si les valeurs entrees dans le constructeur
      sont bien celles que l'on attend.
      """
      if not isinstance(self.egalite, Eq):
         raise TypeError("L'attribut egalite doit etre un objet de type Eq")
      elif not isinstance(self.relation, Relation) and not isinstance(self.relation, Expression):
         raise TypeError("L'attribut relation doit etre un objet de type Relation ou Expression")
