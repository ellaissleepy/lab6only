# SED1515 - Laboratoire 7
# Conversion angle vers PWM

def traduit(degres):
    degres = max(0, min(180, degres))

    impulsion = 500 + 2000 * degres / 180

    return int(impulsion / 20000 * 65535)
