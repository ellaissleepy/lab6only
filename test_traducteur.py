from traducteur_servo import traduit

def tester_traducteur():
    angles = [0, 30, 45, 90, 135, 180]

    for angle in angles:
        resultat = traduit(angle)

        impulsion = 500 + 2000 * angle / 180
        attendu = int(impulsion / 20000 * 65535)

        assert resultat == attendu
        assert 0 <= resultat <= 65535

        print("OK:", angle, "degres =", resultat)

    # Verifier les limites
    assert traduit(-10) == traduit(0)
    assert traduit(200) == traduit(180)

    print("Tous les tests du traducteur ont reussi!")


if __name__ == "__main__":
    tester_traducteur()
