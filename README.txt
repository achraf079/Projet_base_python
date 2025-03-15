Programme de gestion de répertoire téléphonique
==============================================

Description générale
--------------------
Ce programme permet de gérer un répertoire téléphonique simple. Il offre les fonctionnalités suivantes :
1. Ajouter un contact : L'utilisateur peut ajouter un nom et un numéro de téléphone au répertoire.
2. Rechercher un contact : L'utilisateur peut rechercher un nom dans le répertoire et obtenir le numéro de téléphone correspondant.
3. Quitter le programme : L'utilisateur peut quitter le programme à tout moment.

Les données sont stockées dans un fichier texte appelé repertoire.txt.

Fonctionnalités détaillées
--------------------------

1. Ajouter un contact
- L'utilisateur est invité à entrer un nom et un numéro de téléphone.
- Le programme vérifie si le nom existe déjà dans le répertoire :
  - Si le nom existe, un message est affiché pour informer l'utilisateur.
  - Si le nom n'existe pas, le contact est ajouté au fichier repertoire.txt.
- Le numéro de téléphone doit contenir exactement 10 chiffres.

2. Rechercher un contact
- L'utilisateur est invité à entrer un nom à rechercher.
- Le programme parcourt le fichier repertoire.txt pour trouver le nom :
  - Si le nom est trouvé, le numéro de téléphone correspondant est affiché.
  - Si le nom n'est pas trouvé, un message "Inconnu" est affiché.

3. Menu principal
- Le menu principal est affiché en boucle jusqu'à ce que l'utilisateur choisisse de quitter.
- Les options disponibles sont :
  - 0 : Quitter : Arrête le programme.
  - 1 : Ajouter un contact : Permet d'ajouter un nouveau contact.
  - 2 : Rechercher un contact : Permet de rechercher un contact existant.

Fichiers utilisés
-----------------
- repertoire.txt : Fichier texte où sont stockés les contacts. Chaque ligne contient un nom et un numéro de téléphone, séparés par une virgule. Exemple :
  toto,0425213658
  titi,0123456789

Comment utiliser le programme
----------------------------
1. Exécutez le programme Python.
2. Le menu principal s'affiche :
   Bienvenue dans le répertoire téléphonique!
   0: Quitter
   1: Ajouter un contact
   2: Rechercher un contact
3. Choisissez une option en entrant le numéro correspondant :
   - 0 : Pour quitter le programme.
   - 1 : Pour ajouter un contact.
   - 2 : Pour rechercher un contact.

Exemples d'utilisation
----------------------

1. Ajouter un contact
Entrez le nom du contact: Alice
Entrez le numéro de téléphone du contact: 1234567890
Le contact a été ajouté dans le répertoire.

2. Rechercher un contact
Entrez le nom du contact: Alice
Le numéro recherché est : 1234567890

3. Rechercher un contact inconnu
Entrez le nom du contact: Bob
Le contact n'existe pas dans le répertoire.

4. Quitter le programme
Au revoir!

Documentation des fonctions
--------------------------

1. ecriture()
- Description : Ajoute un contact au répertoire téléphonique.
- Paramètres : Aucun.
- Retour : Aucun.
- Fichier modifié : repertoire.txt.

2. lecture()
- Description : Recherche un contact dans le répertoire téléphonique.
- Paramètres : Aucun.
- Retour : Aucun.
- Fichier utilisé : repertoire.txt.

3. menu()
- Description : Affiche le menu principal et gère les interactions de l'utilisateur.
- Paramètres : Aucun.
- Retour : Aucun.

Remarques
---------
- Le fichier repertoire.txt est créé automatiquement s'il n'existe pas.
- Les noms et numéros de téléphone sont stockés au format texte.
- Le programme gère les doublons en vérifiant si un nom existe déjà avant de l'ajouter.

Auteur
------
Ce programme a été développé par Achraf079.