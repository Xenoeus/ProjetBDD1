class Relation:
	"""
	Cette classe represente une relation en SPJRUD ou une table en SQL.
	"""
    
    def __init__(self, nom, attributs):
    	self.nom = nom
    	self.attributs = attributs

    def __str__(self):
    	return self.nom