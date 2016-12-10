from Expression import Expression

class Attribut(Expression):
	"""
	Cette classe represente un attribut d'une relation en SPJRUD
	ou le nom d'une colonne d'une table en SQL.
	"""

    def __init__(self, nom):
    	self.nom = nom

    def __str__(self):
    	return self.nom