def teil_a():
    # Person A arbeitet hier
    summe = 0
    for i in range(1, 500001):
        if i % 7 == 0 and i % 5 != 0:
            summe += i
    return summe




def teil_b():
    #Person B arbeitet hier
    return 0

print(teil_a())

#die letzen 3 ziffer sind die Lösung