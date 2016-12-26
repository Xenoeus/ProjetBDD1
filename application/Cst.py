from Expression import Expression

class Cst(Expression):
   """
   Cette classe represente une constante.
   Par exemple : Une valeur a l'interieur d'une table en SQL.
   """
   def __init__(self, nom):
      self.nom = nom
      self.nomExpression = "Cst("+nom+")"

   def __str__(self):
      return "'"+self.nom+"'"
