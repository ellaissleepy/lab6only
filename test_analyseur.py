from analyseur_gcode import analyser_ligne

def tester_analyseur():
    tests = [
        ("G1 S90 E45", "G1", {"S": 90.0, "E": 45.0}),
        ("G1 S60", "G1", {"S": 60.0}),
        ("G1 E30", "G1", {"E": 30.0}),
        ("M3", "M3", {}),
        ("M5", "M5", {}),
        ("M18", "M18", {}),
        ("", None, {}),
        ("G1 S47.847 E57.273", "G1",
         {"S": 47.847, "E": 57.273})
    ]

    for ligne, attendu, params_attendus in tests:
        commande, params = analyser_ligne(ligne)

        assert commande == attendu
        assert params == params_attendus

        print("OK:", repr(ligne))

    print("Tous les tests de l'analyseur ont reussi!")


if __name__ == "__main__":
    tester_analyseur()
