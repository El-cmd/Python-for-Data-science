from give_bmi import give_bmi, apply_limit

if __name__ == "__main__":
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        # volontairement pas la même taille pour tester l'erreur
        # Calcul du BMI
        bmi = give_bmi(height, weight)
        print("Liste des IMC :", bmi, type(bmi))

        # Application d'une limite
        limit_result = apply_limit(bmi, 26)
        print("Résultats du filtre :", limit_result, type(limit_result))

    except (TypeError, ValueError) as e:
        print(f"Erreur : {e}")
