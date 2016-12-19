import sqlite3
from Relation import Relation

class Expression:

   """
   Cette classe represente une expression SPJRUD. C'est la classe mere de tout les objets
   de notre AST.
   """

   def __init__(self, relation):
      print(string(relation))
      self.relation = relation
      self.colonnes = relation.colonnes


   def print_query(self):
      print(self.query)
   def string_query(self):
      return (self.query)
