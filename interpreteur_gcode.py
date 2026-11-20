# SED1515 - Laboratoire 7
# Interpreteur des commandes G-code

from time import sleep
from traducteur_servo import traduit

# These pen angles must be calibrated
ANGLE_STYLO_HAUT = 0
ANGLE_STYLO_BAS = 30

def deplacer_servo(servo, angle):
    if angle < 0 or angle > 180:
        raise ValueError("Angle hors limites")

    servo.duty_u16(traduit(angle))
    sleep(0.5)

def executer_commande(commande, parametres, servos):

    if commande == "G1":
        if "S" in parametres:
            deplacer_servo(
                servos["epaule"],
                parametres["S"]
            )

        if "E" in parametres:
            deplacer_servo(
                servos["coude"],
                parametres["E"]
            )

    elif commande == "M3":
        deplacer_servo(
            servos["stylo"],
            ANGLE_STYLO_BAS
        )

    elif commande == "M5":
        deplacer_servo(
            servos["stylo"],
            ANGLE_STYLO_HAUT
        )

    elif commande == "M18":
        for servo in servos.values():
            servo.duty_u16(0)

    else:
        print("Commande inconnue:", commande)
