# SED1515 - Laboratoire 7
# Programme principal du traceur robotique

from machine import Pin, PWM
from analyseur_gcode import analyser_ligne
from interpreteur_gcode import executer_commande

PIN_EPAULE = 0
PIN_COUDE = 1
PIN_STYLO = 2


def initialiser_servos():
    epaule = PWM(Pin(PIN_EPAULE))
    coude = PWM(Pin(PIN_COUDE))
    stylo = PWM(Pin(PIN_STYLO))

    servos = {
        "epaule": epaule,
        "coude": coude,
        "stylo": stylo
    }

    for servo in servos.values():
        servo.freq(50)

    return servos


def lire_gcode(nom_fichier, servos):
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            commande, parametres = analyser_ligne(ligne)

            if commande is not None:
                print("Commande:", commande)
                print("Parametres:", parametres)

                executer_commande(
                    commande,
                    parametres,
                    servos
                )


def main():
    servos = initialiser_servos()

    try:
        lire_gcode("ligne.gcode", servos)
        print("Programme termine")

    except Exception as erreur:
        print("Erreur:", erreur)

    finally:
        for servo in servos.values():
            servo.duty_u16(0)


if __name__ == "__main__":
    main()
