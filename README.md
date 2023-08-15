- Bonjour, voici notre projet python 

- C' est une application web développé avec FastApi en backend et ReactJS en frontend et POSTGRESQL(base de donné)

- Notre thème est 'GESTION DE LA RESERVATION D' UN CHAMBRE DANS UN HOTEL' 

- Les APIs de notre application sont protégés, on ne peut pas utiliser les APIs si on ne serait pas connecté 

- On a utilisé JWT(JSON Web Tokens) pour protégé les APIs et faire de session des utilisateurs

- Voici comment se deroule la fonctionnalité de notre application :

        1 - notre application permet d'ajouter, lister, supprimer et mettre à jour des tables clients, chambres et reservations

        2 - pour faire une nouvelle réservation, l' application doit vérifier si la chambre est occupé ou pas. Si occupé donc la réservation ne peut pas être ajouter

        3 - en plus, nous avons géré cette fonctionnalité qui peut vérifier l' occupation d' une chambre à partir d' une date si la chambre est occupé à la date demandé alors la réservation est réjetté

- Pour faire fonctionner l' application après le clonage:
         <!-- configuration pour le backend -->
        1 - déplacement cd backend/
        2 - création une virtual d' environnement
        3 - activation de virtual d'environnement
        4 - lancement du commande ' pip install requirements.txt '
        
        ***********************************************************************************************************

         <!-- configuration de la base de donné -->
        1 - il faut avoir la base de donnée nommé 'reservation_chambre'
        2 - on peut modifier la connexion dans le fichier 'services/config.py'
        3 - puis on démarre l'application avec la commande 'uvicorn main:app --reload

        ************************************************************************************************************

        <!-- création d'un nouveau utilisateur de l' application -->
        1 - après le démarrage de l'application on tape dans la bar d'URL d'un navigateur http://localhost:8000/docs
        2 - et on a beaucoup des API 
        3 - on touche juste sur l'api titré 'API USERS' et il y a une api qui s' appelle '/api/user/signup/' create user et entré un utilisateur

        ************************************************************************************************************

        <!-- à propos de la partie frontend -->
        1 - rendez-vous à la racine du dossier de clonage
        2 - déplacement dans le dossier react-admin-vite/
        3 - lancement du commande 'npm install'
        4 - démarrage de l'application avec la commande ' npm run dev '
        5 - on écrit dans la bar d' URL cette adresse 'http://127.0.0.1:5173/login'


- Rangement des dossiers pour python:
        * dans le dossier backend:
                - /api/   --> on retrouve les fichiers pour les traitements des APIs
                - /routers/   --> on rencontre des fichiers qui sert des routes pour nos APIs
                - /services/   --> on y trouve des fichiers des configurations comme la connexion à la base de donné, les schemas, les models
                - /main.py   --> c' est le fichier racine de notre projet 