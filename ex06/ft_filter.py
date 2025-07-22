def ft_filter(function, iterable):
    for x in iterable:
        if function(x):
            yield x  # important pour la liste genere un yield. - de memoire
