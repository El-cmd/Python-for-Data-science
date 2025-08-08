import time
from datetime import datetime

now = time.time()

# Partie 1 : secondes depuis le 1er janvier 1970
# Format décimal avec virgule ,.4f: 1,666,355,857.3622
# Format scientifique ,.2e: 1.67e+09
# Format décimal sans virgule : 1666355857.3622
# Format décimal avec virgule et arrondi à 2 décimales : 1,666,355,857.36
print(f"Seconds since January 1, 1970: {now:,.4f} \
      or {now:.2e} in scientific notation")

# Partie 2 : date formatée
# %b : mois en abrégé
# %d : jour
# %Y : année
# %H : heure
# %M : minute
# %S : seconde
dt = datetime.fromtimestamp(now)
print(dt.strftime("%b %d %Y"))
