liste_connexions=["admin", "user1", "root", "guest", "anonymous"]
for utilisateur in liste_connexions:
    if utilisateur=="admin" or utilisateur== "root":
        print("Alerte: connexion d'un compte privilège")
    else:
        print("Connexion standard")