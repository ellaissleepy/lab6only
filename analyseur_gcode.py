# SED1515 - Laboratoire 7
# Analyseur de G-code

def analyser_ligne(ligne):
    ligne = ligne.split(";")[0].strip().upper()

    if not ligne:
        return None, {}

    elements = ligne.split()
    commande = elements[0]
    parametres = {}

    for element in elements[1:]:
        nom = element[0]
        valeur = float(element[1:])
        parametres[nom] = valeur

    return commande, parametres
