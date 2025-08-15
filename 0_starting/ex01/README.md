# Exercice 01 - Format ft_time

## Description
Manipulation du temps et formatage de dates en Python avec les modules `time` et `datetime`.

## Objectif
Apprendre à travailler avec les timestamps Unix et le formatage de dates.

## Fichiers
- `format_ft_time.py` : Script de formatage temporel

## Concepts abordés
- **Timestamp Unix** : Secondes écoulées depuis le 1er janvier 1970
- **Formatage numérique** : Notation scientifique, séparateurs de milliers
- **Formatage de dates** : Conversion timestamp vers date lisible
- **Module time** : `time.time()` pour obtenir le timestamp actuel
- **Module datetime** : `datetime.fromtimestamp()` et `strftime()`

## Utilisation
```bash
python format_ft_time.py
```

## Sortie attendue
```
Seconds since January 1, 1970: 1,666,355,857.3622       or 1.67e+09 in scientific notation
Oct 21 2022
```

## Formats utilisés
- `{now:,.4f}` : Nombre avec séparateurs de milliers et 4 décimales
- `{now:.2e}` : Notation scientifique avec 2 décimales
- `%b %d %Y` : Mois abrégé, jour, année (ex: "Oct 21 2022")
