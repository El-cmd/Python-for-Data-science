# Module 0_starting - Introduction à Python

## Vue d'ensemble
Ce module constitue une introduction complète aux concepts fondamentaux de Python pour la Data Science. Il couvre les bases du langage, la manipulation de données, et les outils essentiels pour débuter en programmation Python.

## Prérequis
- Python 3.x installé
- Environnement virtuel configuré (voir `venv/`)
- Dépendances installées : `pip install -r requirements.txt`

## Structure du module

### 📁 Exercices disponibles

| Exercice | Nom | Concepts clés |
|----------|-----|---------------|
| **ex00** | Hello World | Structures de données (list, tuple, set, dict) |
| **ex01** | Format ft_time | Manipulation du temps et formatage |
| **ex02** | Find ft_type | Introspection de types avec `type()` |
| **ex03** | NULL not found | Détection des valeurs "nulles" |
| **ex04** | What is | Arguments système et parité |
| **ex05** | Building | Analyse de chaînes de caractères |
| **ex06** | Filter String | Générateurs et filtrage personnalisé |
| **ex07** | SOS | Dictionnaires et code Morse |
| **ex08** | Loading | Barres de progression et `yield` |
| **ex09** | Package | Distribution de packages Python |

## Concepts Python abordés

### 🔧 Fondamentaux
- **Types de données** : `int`, `str`, `list`, `tuple`, `set`, `dict`
- **Structures de contrôle** : `if/elif/else`, boucles `for`
- **Fonctions** : définition, paramètres, valeurs de retour
- **Gestion d'erreurs** : `try/except`, `assert`

### 🚀 Concepts avancés
- **Générateurs** : `yield` et économie mémoire
- **Introspection** : `type()`, `isinstance()`
- **Expressions lambda** : fonctions anonymes
- **Modules système** : `sys.argv`, `time`, `datetime`

### 📦 Outils et bibliothèques
- **Packaging** : `setuptools`, distribution de code
- **Manipulation de chaînes** : méthodes built-in, module `string`
- **Entrées/sorties** : `input()`, formatage d'affichage

## Progression recommandée

1. **ex00-ex03** : Bases du langage et types de données
2. **ex04-ex05** : Arguments système et manipulation de chaînes
3. **ex06-ex08** : Concepts avancés (générateurs, filtrage)
4. **ex09** : Distribution et packaging

## Utilisation

Chaque exercice dispose de son propre README avec :
- Description détaillée
- Exemples d'utilisation
- Concepts techniques expliqués
- Commandes de test

```bash
# Naviguer vers un exercice
cd ex00/

# Consulter la documentation
cat README.md

# Exécuter le code
python Hello.py
```

## Fichiers du module

- **`python0.pdf`** : Sujet complet des exercices
- **`requirements.txt`** : Dépendances Python nécessaires
- **`venv/`** : Environnement virtuel Python
- **`.gitignore`** : Fichiers ignorés par Git

## Objectifs pédagogiques

À la fin de ce module, vous maîtriserez :
- ✅ Les types de données fondamentaux de Python
- ✅ La gestion des arguments et des erreurs
- ✅ Les concepts de générateurs et d'itérateurs
- ✅ La création et distribution de packages Python
- ✅ Les bonnes pratiques de programmation Python

## Support

Chaque exercice contient des exemples pratiques et des cas de test pour valider votre compréhension. Consultez les README individuels pour des détails spécifiques à chaque exercice.
