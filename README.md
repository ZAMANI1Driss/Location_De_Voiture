# Gestion de Location de Voiture

Il s'agit d'une application de Location De Voiture construite à l'aide de Tkinter qui permet aux Admins de
gérer l'application de leur Location De Voiture, et permet aux Utilisateurs de consulter l'application. L'application dispose d'une interface conviviale qui permet aux utilisateurs de consulter les voitures disponibles dans le garage ainsi que l'admin
ayant un but de modifier , ajouter et supprimer les voitures , n'oublions pas que l'Admin peut aussi avoir les memes fonctionnalités de
l'application que l'utilisateur.

## Caractéristiques 

L'application de Location De Voiture comprend les éléments suivants:

- Ajouter des nouvelles voitures à l'application
- Modifier les informations des voitures déjà possédées
- Supprimer des voitures du garage
- Authentification des clients
- Authentification des admins

## Installation

Pour installer l'application de Location De Voiture, suivez ces
étapes :

1. Clonez le référentiel sur votre machine locale.
2. Assurez-vous que Python 3.6 ou version ultérieure est installée sur votre système.
3. Installez les bibliothèques requises en exécutant la commande :
    `pip installer tkinter`.
4. Exécutez l'application en exécutant la commande `python main.py`.
5. Installez Mysql Server, puis ouvrez mysql command line tool et entrez cette commande "/usr/local/mysql/bin/mysql -uroot -p", le mot de passe est "driss123",enfin vous aurez l'accès à la base de données.

## Utilisation 

Une fois que vous avez installé et lancé l'application de Location De Voiture,
vous pouvez l'utiliser pour gérer votre Location De Voiture, et pour le client
avoir les fonctionalités adequates au utilisateur en effectuant les tâches suivantes :

1. S'inscrire à l'application de Location De Voiture
2. Connectez-vous en utilisant votre nom d'utilisateur et votre mot de passe.
3. En tant qu'Admin, ajoutez des voitures pour que le client puisse les voir.
   En tant que Client, cliquez sur le boutton afficher les voitures 
   pour consulter les voitures disponibles.
4. Rechercher les voitures en cliquant sur "Chercher Une voiture"
    bouton et remplissez un ou plusieurs champs. 
5. S'il s'agit d'un admin , il peut ajouter un produit en cliquant sur 'Ajouter Voiture"
    bouton et remplissez les informations requises.
6. S'il s'agit d'un admin , il peut modifier un produit en cliquant sur "Modifier Voiture"
    bouton et remplissez les informations requises.
7. S'il s'agit d'un admin , il peut supprimer un produit en cliquant sur "Supprimer Voiture"
    bouton et remplissez les informations requises.
8. S'il s'agit d'un client , il peut consulter les voitures en cliquant sur "Afficher Voiture"
9. S'il s'agit d'un client , il peut chercher une voiture en cliquant sur "Chercher Voiture"
10. Pour quitter l'application , l'Admin et le Client peuvent cliquer sur "Quitter systeme"
11. Pour Avoir les droits d'un Admin, il faut cliquer sur le bouton "Connect Database", et en remplissant les champs "host" "username" "password".

      ****************************************************************
      *								     *
      *	NB:host = localhost, username = root, password = driss123.   *
      *		 						     *
      *	**************************************************************
      ****************************************************************
      *								     *
      *	NB:les fichiers source code sont nommés:		     *
      *								     *
      *		-main.py					     *
      *		-signin.py					     *
      *		-signup.py					     *
      *	   							     *
      *		 						     *
      *	**************************************************************


## Conception des classes et objets pour gérer les produits et les utilisateurs :


1.	Classe Utilisateur :
•	Attributs :
	id (int) : identifiant unique de l'utilisateur
	email (str) : email de l'utilisateur
	username (str) : username de l'utilisateur
	password (str) : mot de passe de l'utilisateur (stocké sous forme de hash sécurisé)
•	Méthodes :
 	register(username, password,email) : crée un nouvel utilisateur et l'ajoute à la base de données
	login(username, password) : vérifie si le nom d'utilisateur et le mot de passe correspondent à un utilisateur existant

2.	Classe Voitures :
•	Attributs :
	id (str) : identifiant unique de la voiture
	marque (str) : nom de la marque de la voiture
	type_carburant (str) : type de carburant de la voiture
	nombre_de_places (str) : nombre de places dans la voiture
	transmission (str) : type de transmission de la voiture
	prix_de_location (str) : prix de location de la voiture journalière

•	Méthodes :
	add_Voitures() : ajoute une nouvelle voiture a la base de donnees
	update_voiture() : met à jour les informations d'une voiture existant dans la base de donnees
	delete_voiture() : supprime une voiture de la base de donnees
	chercher_voiture() : recherche une voiture selon des critères spécifiés (id,marque,type_carburant,nombre_de_places,transmission,prix_de_location)
	connect_databases() : permet aux Admins de se connecter a la database

## Planification de l'architecture de la base de données :
1.	Table "Utilisateurs" :
•	id : clé primaire,string, non nul,auto incrementé
•	email : string
•	username : string,unique
•	password : string
2.	Table "Voitures" :
•	id : clé primaire,string,non nul
•	marque : string
•	prix_de_location : string
•	transmission : string
•	type_carburant : string
•	nombre_de_places : string

## Credit :

L'application de Location De Voiture est le fruit d'un travail acharné et rigoureux mené par trois étudiantes : ZAMANI Driss, BENFADDOUL Fahd et KHALIL Iyad. Nous avons su allier nos compétences et notre détermination pour concevoir une solution informatique performante et intuitive.
Cependant, un tel succès n'aurait pas été possible sans les précieux conseils et le soutien indéfectible de notre enseignant, Mr.AMEKSA Mohamed. Sa grande expertise en la matière et sa passion pour l'informatique ont été des atouts majeurs pour le développement de l'application. Nous tenons donc à exprimer notre profonde gratitude envers Mr.AMEKSA Mohamed, qui a su nous guider et nous inspirer ces  tout au long de notre projet.
