import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst):
        # calcul du pourcentage (entre 0 et 100)
        percent = (i + 1) / total * 100
        # longueur de la barre (en nombre de caractères)
        bar_length = 66
        # combien de blocs "█" on affiche
        done = int(bar_length * (i + 1) / total)
        # créer la barre avec des "█" et des "-"
        bar = "█" * done + "-" * (bar_length - done)
        # écrire sur la même ligne grâce à '\r'
        sys.stdout.write(f"\r{int(percent):3}%|{bar}| {i + 1}/{total}")
        sys.stdout.flush()
        yield item
