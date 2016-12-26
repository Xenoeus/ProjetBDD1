# ProjetBDD1
Ce projet a été réalisé par Pierre Zielinski et Robin Libert pour le cours de Base de donnée 1.

Ce projet de base de donnée consiste à traduire une expression SPJRUD en une requête SQL.
Nous avons choisis de créer un objet pour chaque élément d'une expression SPJRUD.
Pour ce faire, nous nous sommes inspirés de la figure 1 des consignes. Chaque expression SPJRUD descend de la classe mère Expression.
Chaque paramètres d'une expression SPJRUD est un objet de la librairie. Au moment ou la requête en SPJRUD est envoyé à la classe "Traducteur", celle-ci instancie chaque Objet.
Au moment où chaque objet est istancier, les verifications se lance et vérifie que tout est bien correct et bien rentré.
Si jamais quelque chose est incorect (un élément est incorrect si: ce n'est pas l'élément que l'on attendais, ce n'est pas le bon type d'élément ou que cet élémént n'existait pas) alors une erreur est renvoyée.
La classe qui gère le tout est la classe "SPRJUDToSQL", celle-ci comprends quate méthode, dont trois pour la traduction et/ou l'execution.
Si une erreur est renvoyée alors ces méthodes la récupèrerons et la renverrons sous forme de String à la console(explication ci-dessous(Mode d'emploi)).

Nous avons rencontré qu'un seul problème majeur qui fut que nous avions d'abord mis les verification dans l'initialisation mais alors nous ne savions pas récupérer les erreurs.
Nous avons donc séparer les vérifications de l'initialisation.
Un autre problème que nous avons rencontré mais qui n'a pas été important, c'est que en recherchant des commande pour sqlite nous en avons trouvé qui ne fonctionnais pas sur Python (ce n'était pas indiqué sur les sites bien-sûr).
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Mode d'emploi:
--------------
Pour utiliser cette librairie vous devez importer la classe "SPRJUDToSQL" (Celle-ci contient quatre méthode).
Avant tout vous devez lui fournir votre base de donnée en la rentrant grâçe à la méthode: "selectionDataBase" 

Les méthodes sont:
-selectionDataBase(Database): Cette méthode prend en paramètre la Base de donnée que vous voulez utiliser.
(Les méthodes de cette classe utilisée après l'appel à cette méthode prendrons la base de donnée envoyée comme référence)

-traduction(SPJRUD): Cette méthode traduis une requête SPJRUD en SQL.
Elle prend en paramètre une requête en SPJRUD.
Cette méthode envoi à la console la requête traduite et renvoi True si tout c'est bien passé.
Sinon, elle envoie à la console le problème rencontré et renvoi False.

-traductionEtExecution(SPJRUD): Cette méthode traduis et exécute une requête SPJRUD en SQL.
Elle prend en paramètre une requête en SPJRUD.
Cette méthode envoi à la console la requête traduite, ainsi que la table obtenue et renvoi True si tout c'est bien passé.
Sinon, elle envoie à la console le problème rencontré et renvoi False.

-traductionEtCreationDeTable(SPJRUD , Nom): Cette méthode traduis et exécute une requête SPJRUD en SQL et créée une table avec le résultat.
Elle prend en paramètre une requête en SPJRUD.
Cette méthode envoi à la console la requête traduite, ainsi que la table créée (qui est placée dans la table de donée)et renvoi True si tout c'est bien passé.
Sinon, elle envoie à la console le problème rencontré et renvoi False.


--------------
Formulation:
--------------
Les requête SPRJUD doivent être écrite sous cette forme:

- Attribut(nom): Prend le nom de l'attribut(du nom de colonne) en paramètre.
- Cst(nom): Prend le nom de la constante/la constante en paramètre.
- Relation(nom): Prend le nom de la relation en paramètre.
- Eq(Attribut1, Attribut2, signe): Prend un attribut/constante, un attribut/constante et le signe en paramètre.
- Difference(Relation1,Relation2): Prend une relation/expression et une relation/expression en paramètre.
- Join(Relation1,Relation2): Prend une relation/expression et une relation/expression en paramètre.
- Union(Relation1,Relation2): Prend une relation/expression et une relation/expression en paramètre.
- Project(Attribut,Relation): Prend une liste d'attributs et une relation/expression en paramètre.
- Rename(nom_initial, nouveau_nom, relation): Prend une l'ancien nom de la colonne , le nouveau nom de la colonne et une relation/expression en paramètre.
- Select(egalite, relation): Prend une inégalité(Eq) et une relation/expression en paramètre.


Exemple de requête valide:
traducteur.traductionEtExecution(Select(Eq(Attribut('Name'), Cst('Bergen'), "="), Relation('CITY')))

