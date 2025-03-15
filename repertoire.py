# Description: Programme qui permet de gérer un répertoire téléphonique
# Auteur: Achraf079


# La fonction lecture() permet de rechercher un numero de téléphone associeé au nom rentrer par l'utilisateur dans le répertoire téléphonique
def lecture():
    nom_recherche = input("Entrez le nom du contact: ")
    try:
        with open('repertoire.txt', 'r') as fichier:
            for ligne in fichier:
                nom_fichier, telephone = ligne.strip().split(',')
                if nom_fichier == nom_recherche:
                    print(f"Le numéro recherché est : {telephone}")
                    return
        print("Le contact n'existe pas dans le répertoire.")

    except FileNotFoundError:
        print("Le répertoire est vide ou n'existe pas encore.")

# La fonction ecriture() permet d'ajouter un contact dans le répertoire téléphonique
# Le nom et le numéro de téléphone du contact sont rentrés par l'utilisateur


def ecriture():

    while True:
        nom = input("Entrez le nom du contact: ").strip()
        if nom:  # Vérifie que le nom n'est pas vide
            break
        print("Le nom ne peut pas être vide. Veuillez réessayer.")

    try:
        with open('repertoire.txt', 'r') as fichier:
            lignes = fichier.readlines()  # Lit toutes les lignes du fichier
    except FileNotFoundError:
        # Si le fichier n'existe pas, initialise une liste vide
        lignes = []

    contact_existe = False

    # Parcours chaque ligne du fichier
    for ligne in lignes:
        nom_fichier, _ = ligne.strip().split(',')
        if nom_fichier == nom:
            print("Le contact existe déjà dans le répertoire.")
            contact_existe = True
            break
    if not contact_existe:
        while True:
            telephone = input(
                "Entrez le numéro de téléphone du contact: ").strip()
            # Vérifie que le numéro est valide et contient 10 chiffres
            if telephone.isdigit() and len(telephone) == 10:
                break
            print("Le numéro de téléphone doit contenir 10 chiffres. Veuillez réessayer.")

        try:
            with open('repertoire.txt', 'a') as fichier:
                fichier.write(f"{nom},{telephone}\n")
                print("Le contact a été ajouté dans le répertoire.")

        except FileNotFoundError:
            print("Le répertoire est vide ou n'existe pas encore.")

    contact_existe = False


# La fonction menu() permet d'afficher le menu principal du répertoire téléphonique
# L'utilisateur peut ajouter un contact, rechercher un contact ou quitter le programme

def menu():
    while True:
        commande = input(
            "Bienvenue dans le répertoire téléphonique! \n 0: Quitter \n 1: Ajouter un contact \n 2: Rechercher un contact \n")

        if commande == "1":
            ecriture()

        elif commande == "2":
            lecture()

        elif commande == "0":
            print("Au revoir!")
            exit()

        else:
            print("Commande invalide. Veuillez choisir une option valide.")


menu()
