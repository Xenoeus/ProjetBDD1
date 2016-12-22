# ProjetBDD1
Ce projet de base de donnée consiste à traduire une expression SPJRUD en une requête SQL.
Nous avons choisis de créer un objet pour chaque élément d'une expression SPJRUD.
Pour ce faire, nous nous sommes inspirés de la figure 1 des consignes. Chaque expression SPJRUD descend de la classe mère Expression.
Chaque paramètres d'une expression SPJRUD est un objet de la librairie. Chaque fois que l'on instancie un objet, on vérifie que ses paramètres sont bien ceux que l'on attend, si ce n'est pas le cas on renvoit une erreur qui indique à l'utilisateur quel objet correspond au paramètre. Nous utilisons une méthode qui représente l'équivalent de chaque expression SPJRUD en SQL et chaque fois que l'on instancie une expression, cette méthode est appelée.
