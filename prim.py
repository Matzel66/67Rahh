from datetime import datetime

def ist_primzahl(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def finde_te_primzahl(ziel_anzahl):
    zeler = 0
    zahl = 2
    
    while zeler < ziel_anzahl:
        if ist_primzahl(zahl):
            zeler += 1
            if zeler == ziel_anzahl:
                return zahl
        zahl += 1

n = 1000
ergebnis = finde_te_primzahl(n)


current_year = datetime.now().year

ende= int(ergebnis) + int(current_year)
print(ende)